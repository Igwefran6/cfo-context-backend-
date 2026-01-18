from datetime import datetime
from app.value.pricing import ANALYST_HOURLY_RATE, EVENT_PRICING_MINUTES


def log_value_event(client_id: str, event_type: str, description: str) -> dict:
    minutes = EVENT_PRICING_MINUTES[event_type]
    value_usd = round((minutes / 60) * ANALYST_HOURLY_RATE, 2)

    return {
        "client_id": client_id,
        "event_type": event_type,
        "description": description,
        "minutes_saved": minutes,
        "value_usd": value_usd,
        "timestamp": datetime.utcnow().isoformat(),
    }