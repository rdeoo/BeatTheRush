# Easeway

Easeway is a mobile-first web app that creates personalized commute schedules.

This repository contains the **FastAPI backend**.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn

## Project Structure

```
easeway-backend/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── core/            # Config and settings
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas
│   ├── routers/         # API routes
│   └── services/        # Business logic (e.g. Google Maps wrapper)
├── requirements.txt
├── .env.example
└── README.md
```