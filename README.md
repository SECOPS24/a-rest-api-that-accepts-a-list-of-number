# Numbers Statistics API

A lightweight REST API built with **FastAPI** that accepts a list of numbers and returns statistical values: sum, average, maximum, and minimum.

---

## Features

- **POST /statistics** — Compute statistics for a list of numbers
- **GET /health** — Health check endpoint
- **GET /docs** — Interactive Swagger UI
- **GET /redoc** — ReDoc API documentation
- Input validation with clear error messages
- Supports integers and floating-point numbers

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker (optional)

---

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python main.py
```

The API will be available at `http://localhost:3000`.

---

### Run with Docker

```bash
# Build the image
docker build -t numbers-stats-api .

# Run the container
docker run -p 3000:3000 numbers-stats-api
```

---

## API Reference

### `POST /statistics`

Accepts a JSON body with a list of numbers and returns statistical results.

**Request Body:**

```json
{
  "numbers": [10, 20, 30, 40, 50]
}
```

**Response:**

```json
{
  "count": 5,
  "numbers": [10.0, 20.0, 30.0, 40.0, 50.0],
  "sum": 150.0,
  "average": 30.0,
  "maximum": 50.0,
  "minimum": 10.0
}
```

**Example with `curl`:**

```bash
curl -X POST http://localhost:3000/statistics \
  -H "Content-Type: application/json" \
  -d '{"numbers": [10, 20, 30, 40, 50]}'
```

---

### `GET /health`

Returns the health status of the API.

**Response:**

```json
{ "status": "ok" }
```

---

## Error Handling

| Scenario | HTTP Status | Message |
|---|---|---|
| Empty list provided | `422 Unprocessable Entity` | The list of numbers must not be empty. |
| Invalid JSON body | `422 Unprocessable Entity` | Validation error details |
| Non-numeric values | `422 Unprocessable Entity` | Validation error details |

**Example error response:**

```json
{
  "detail": [
    {
      "loc": ["body", "numbers"],
      "msg": "The list of numbers must not be empty.",
      "type": "value_error"
    }
  ]
}
```

---

## Project Structure

```
.
├── main.py            # Application entry point
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container definition
└── README.md          # This file
```

---

## Interactive Docs

Once the server is running, visit:

- **Swagger UI:** [http://localhost:3000/docs](http://localhost:3000/docs)
- **ReDoc:** [http://localhost:3000/redoc](http://localhost:3000/redoc)
