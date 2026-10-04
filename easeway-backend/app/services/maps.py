import httpx
from app.core.config import settings

ROUTES_URL = "https://routes.googleapis.com/directions/v2:computeRoutes"

class MapsError(Exception):
    """Raised when Google Maps request fails or returns no usable result."""


async def get_estimated_duration(origin: str, destination: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": settings.GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "routes.duration,routes.distanceMeters",
    }
    body = {
        "origin": {"address": origin},
        "destination": {"address": destination},
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(ROUTES_URL, json=body, headers=headers)
    except httpx.RequestError:
        raise MapsError("Could not reach Google Maps. Try again later.")

    routes = response.json().get("routes")
    if not routes:
        raise MapsError("No route found between these locations.")

    route = routes[0]
    seconds = int(float(route["duration"].rstrip("s")))

    return {
        "duration_seconds": seconds,
        "distance_meters": route.get("distanceMeters", 0)
    }
