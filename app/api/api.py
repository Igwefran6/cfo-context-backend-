"""
API Endpoints

This file defines all /api routes for the CFO context demo.

Responsibilities:
- Expose read-only, demo-safe endpoints
- No business logic
- No AI orchestration
- No side effects outside value logging
"""

from fastapi import APIRouter

from app.context.builder import build_context_snapshot
from app.value.logger import log_value_event

router = APIRouter()


@router.get("/clients/{client_id}/context")
def get_client_context(client_id: str):
    """
    Return a CFO-ready context snapshot for the given client.

    This is the core demo endpoint:
    CFO opens app → selects client → instantly regains context.
    """
    snapshot = build_context_snapshot(client_id)
    return snapshot.model_dump()


@router.get("/clients/{client_id}/roi")
def get_client_roi(client_id: str):
    """
    Return audit-defensible ROI metrics for the client.

    This powers the 'Practice Leverage Dashboard'.
    """
    snapshot = build_context_snapshot(client_id)

    return {
        "client_id": client_id,
        "total_value_generated": snapshot.total_value_generated,
        "value_events": snapshot.value_events,
    }


@router.post("/clients/{client_id}/export")
def export_narrative(client_id: str):
    """
    Simulate exporting a narrative to a client.

    This is a VERIFIED VALUE EVENT:
    CFOs do not send bad reports to clients.
    """
    return log_value_event(
        client_id=client_id,
        event_type="narrative_exported",
        description="Narrative exported to client"
    )


@router.post("/clients/{client_id}/slack/draft")
def draft_slack_reply(client_id: str):
    """
    Simulate drafting a Slack reply using client context.

    This demonstrates:
    - AI agent assistance
    - Capacity unlock
    - No autonomous sending
    """
    value_event = log_value_event(
        client_id=client_id,
        event_type="slack_draft_reply",
        description="Slack reply drafted"
    )

    return {
        "draft": (
            "Here’s a draft reply based on the latest client context:\n\n"
            "Cash runway is tight at ~5 months. I recommend we pause hiring "
            "and review burn before committing to new spend."
        ),
        "value_event": value_event,
    }