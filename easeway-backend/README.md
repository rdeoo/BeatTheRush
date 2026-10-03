# Easeway

Easeway is a mobile-first web app that creates personalized commute schedules.

This directory contains the **FastAPI backend**.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn

## Project Structure

```
.
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

## Getting Started

1. Clone the repository

```bash
git clone <repo-url>
cd easeway-backend
```

2. Create and activate virtual enironment

```bash
python -m venv .venv
source venv/bin/activate # Windows: source venv/Scripts/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```