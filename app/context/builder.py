"""
Context Builder

Constructs a CFO-ready Context Snapshot.
This is a meaning-making layer, not data access.

NOTE:
Value events here are logged in DEMO MODE.
In production, value logging would be tied to explicit user actions.
"""

from datetime import datetime
from typing import List, Dict, Union

from pydantic import BaseModel

from app.value.logger import log_value_event


# ---------------- Models ----------------

class Alert(BaseModel):
    type: str
    severity: str
    message: str


class OpenDecision(BaseModel):
    id: str
    question: str
    severity: str


class LastInteraction(BaseModel):
    type: str
    date: str
    summary: str


class ContextSnapshot(BaseModel):
    client_id: str
    generated_at: str
    headline: str
    alerts: List[Alert]
    key_metrics: Dict[str, Union[float, int]]
    recent_changes: List[str]
    open_decisions: List[OpenDecision]
    last_interaction: LastInteraction
    value_events: List[Dict]
    total_value_generated: float


# ---------------- Builder ----------------

def build_context_snapshot(client_id: str) -> ContextSnapshot:

    # Demo metrics
    current_metrics = {
        "cash_balance": 4_200_000.0,
        "monthly_burn": 810_000.0,
        "runway_months": 5.2,
        "revenue_mom_growth": 0.06,
        "days_since_last_contact": 7,
    }

    # Recent changes
    recent_changes = [
        "AWS spend increased 18% MoM"
    ]

    # Alerts
    alerts: List[Alert] = []
    if current_metrics["runway_months"] < 6:
        alerts.append(
            Alert(
                type="runway",
                severity="high",
                message=f"Cash runway at {current_metrics['runway_months']} months"
            )
        )

    headline = (
        f"Cash runway at {current_metrics['runway_months']} months - focus on burn control"
        if alerts else
        "Financial position stable"
    )

    open_decisions = [
        OpenDecision(
            id="dec_001",
            question="Approve Q2 hiring plan?",
            severity="high"
        )
    ]

    last_interaction = LastInteraction(
        type="client_call",
        date="2026-01-05",
        summary="Discussed burn rate and Q1 hiring plan"
    )

    # ---------------- VALUE LOGGING (DEMO MODE) ----------------

    value_events = []

    value_events.append(
        log_value_event(
            client_id=client_id,
            event_type="portfolio_refresh",
            description="Client context refreshed"
        )
    )

    value_events.append(
        log_value_event(
            client_id=client_id,
            event_type="narrative_generated",
            description="CFO narrative drafted"
        )
    )

    if alerts:
        value_events.append(
            log_value_event(
                client_id=client_id,
                event_type="sentinel_alert",
                description="Runway risk detected"
            )
        )

    total_value = sum(event["value_usd"] for event in value_events)

    return ContextSnapshot(
        client_id=client_id,
        generated_at=datetime.utcnow().isoformat(),
        headline=headline,
        alerts=alerts,
        key_metrics=current_metrics,
        recent_changes=recent_changes,
        open_decisions=open_decisions,
        last_interaction=last_interaction,
        value_events=value_events,
        total_value_generated=total_value,
    )