# Weather API

A RESTful API for retrieving weather information for cities around the world. Built with Node.js and Express.

## Features

- Get current weather data for a city
- Fetch weather forecasts
- Supports JSON responses
- Easy to integrate with frontend applications

## Technologies Used

- Node.js
- Express.js
- Axios (for external API requests)
- dotenv (for environment variables)

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-api.git
   cd weather-api
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the root directory and add your weather API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

### Running the Server

```bash
npm start
```

The server will start on `http://localhost:3000` by default.

## API Endpoints

### Get Current Weather

- **Endpoint:** `/api/weather/current`
- **Method:** `GET`
- **Query Parameters:**
  - `city` (required): Name of the city

**Example Request:**
```
GET /api/weather/current?city=London
```

**Example Response:**
```json
{
  "city": "London",
  "temperature": 15,
  "description": "Partly cloudy",
  "humidity": 70
}
```

### Get Weather Forecast

- **Endpoint:** `/api/weather/forecast`
- **Method:** `GET`
- **Query Parameters:**
  - `city` (required): Name of the city
  - `days` (optional): Number of days for the forecast (default: 3)

**Example Request:**
```
GET /api/weather/forecast?city=London&days=5
```

**Example Response:**
```json
{
  "city": "London",
  "forecast": [
    { "date": "2024-06-01", "temperature": 16, "description": "Sunny" },
    { "date": "2024-06-02", "temperature": 14, "description": "Rainy" }
    // ...
  ]
}
```

## Environment Variables

- `WEATHER_API_KEY`: Your API key for the external weather service.

## Error Handling

All errors are returned in JSON format:
```json
{
  "error": "City not found"
}
```

## License

MIT

## Contact

For questions or support, contact [your.email@example.com](mailto:your.email@example.com).
