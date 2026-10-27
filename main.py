from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import List
import uvicorn

app = FastAPI(
    title="Numbers Statistics API",
    description="A REST API that accepts a list of numbers and returns their sum, average, and maximum value.",
    version="1.0.0"
)


class NumbersRequest(BaseModel):
    numbers: List[float]

    @validator("numbers")
    def numbers_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("The list of numbers must not be empty.")
        return v


class StatisticsResponse(BaseModel):
    count: int
    numbers: List[float]
    sum: float
    average: float
    maximum: float
    minimum: float


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/statistics", response_model=StatisticsResponse, tags=["Statistics"])
def compute_statistics(request: NumbersRequest):
    """
    Accepts a list of numbers and returns:
    - **sum**: Total sum of all numbers
    - **average**: Arithmetic mean of the numbers
    - **maximum**: Largest number in the list
    - **minimum**: Smallest number in the list
    - **count**: How many numbers were provided
    """
    numbers = request.numbers
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return StatisticsResponse(
        count=len(numbers),
        numbers=numbers,
        sum=total,
        average=average,
        maximum=maximum,
        minimum=minimum
    )


@app.get("/", tags=["Root"])
def root():
    """Root endpoint with API information."""
    return {
        "name": "Numbers Statistics API",
        "version": "1.0.0",
        "description": "Submit a list of numbers to get statistics.",
        "endpoints": {
            "POST /statistics": "Compute sum, average, maximum, and minimum of a list of numbers",
            "GET /health": "Health check",
            "GET /docs": "Interactive Swagger UI documentation",
            "GET /redoc": "ReDoc documentation"
        },
        "example_request": {
            "url": "POST /statistics",
            "body": {"numbers": [10, 20, 30, 40, 50]}
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
