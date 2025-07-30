# 🌀 Weather-API — Flask App with Caching and Rate Limiting

A Flask-based web app that fetches weather information using the Visual Crossing API. It includes Redis caching and rate-limiting via `Flask-Limiter` to improve performance and control request usage.

---

## 🚀 Features

- ☀️ Fetch real-time weather for any location using Visual Crossing.
- 🚀 Redis caching for faster repeated queries.
- 🛡️ API rate limiting (200/day, 50/hour per IP).
- 🖥️ Clean web interface built with HTML & JS.
- 🔐 Environment-based API key management.

---

## 🧱 Tech Stack

- [Flask](https://flask.palletsprojects.com/)
- [Redis](https://redis.io/)
- [Flask-Limiter](https://flask-limiter.readthedocs.io/)
- [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/sachinsr11/Weather-Api.git
cd Weather-Api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set the API Key

Create a `.env` file or set the environment variable manually:

```bash
export WEATHER_API_KEY=your_visual_crossing_api_key
```

### 4. Start Redis (Required)

Make sure Redis is running locally on port `6379`:
```bash
redis-server
```

### 5. Run the App

```bash
python main.py
```

Go to `http://localhost:5000` and start querying!

---

## 🔁 Example Usage (API)

```
GET /London?start=2023-07-01&end=2023-07-03
```

Returns weather data for London between the given dates.

---

## 🧠 Notes

- Redis cache duration: 2 hours.
- Flask runs in debug mode — disable in production.
- Rate limits are enforced per IP using Redis as a backend.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.
