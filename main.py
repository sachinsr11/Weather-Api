from flask import Flask, request, jsonify, render_template, make_response
import urllib3, json, os
import certifi
import redis
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Configuration for Redis
redis_host = 'localhost'
redis_port = 6379
redis_password = None
redis_expiry = 60*60*2  # 2 hours

# Initialize Redis client
r = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password
)

# Initialize Flask-Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=f"redis://{redis_host}:{redis_port}/0"
)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route for fetching weather data
@app.get("/<location>")
def get_weather(location):
    filterstart = request.args.get('start', "")
    filterend = request.args.get('end', "")
    redisKey = location + filterstart + filterend

    # Try to get data from cache
    try:
        storedData = r.get(redisKey)
        if storedData:
            return jsonify(json.loads(storedData.decode('utf-8')))
    except redis.RedisError as redis_error:
        logging.error(f"Redis error: {redis_error}")
        return make_response(jsonify({"error": f"Redis error: {redis_error}"}), 500)

    # Fetch from API otherwise
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        logging.error("Weather API key is not set.")
        return make_response(jsonify({"error": "API key is missing"}), 500)

    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{filterstart}/{filterend}/?key={api_key}'
    logging.info(f"Requesting URL: {url}")

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    try:
        response = http.request('GET', url, timeout=5.0)
        if response.status == 200:
            try:
                r.setex(redisKey, time=redis_expiry, value=response.data)
            except redis.RedisError as redis_error:
                logging.error(f"Failed to cache in Redis: {redis_error}")
                return make_response(jsonify({"error": f"Failed to cache in Redis: {redis_error}"}), 500)

            return jsonify(json.loads(response.data.decode('utf-8'))), 200

        elif response.status == 401:
            logging.error(f"Unauthorized access: Invalid API key.")
            return make_response(jsonify({"error": "Unauthorized access: Invalid API key."}), 401)

        else:
            logging.error(f"Data return error: {response.status}")
            return make_response(jsonify({"error": f"Request failed with status: {response.status}"}), 500)

    except urllib3.exceptions.HTTPError as http_error:
        logging.error(f"HTTP error occurred: {http_error}")
        return make_response(jsonify({"error": f"HTTP error occurred: {http_error}"}), 400)
    except urllib3.exceptions.RequestError as request_error:
        logging.error(f"Request error occurred: {request_error}")
        return make_response(jsonify({"error": f"Request error occurred: {request_error}"}), 400)
    except Exception as other_error:
        logging.error(f"Other error occurred: {other_error}")
        return make_response(jsonify({"error": f"An unexpected error occurred: {other_error}"}), 500)

if __name__ == '__main__':
    app.run(debug=True)
