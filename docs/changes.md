# Backend Changes – Frontend Integration Required

**Date:** 2026-01-18  
**Purpose:** Document API changes from upstream sync for frontend integration

---

## New API Endpoints

### 1. `GET /api/clients/{client_id}/roi`

Returns audit-defensible ROI metrics for the client.

**Response:**

```json
{
  "client_id": "client_acme",
  "total_value_generated": 75.0,
  "value_events": [...]
}
```

---

### 2. `POST /api/clients/{client_id}/export`

Simulates exporting a narrative to a client. Logs a verified value event.

**Response:**

```json
{
  "client_id": "client_acme",
  "event_type": "narrative_exported",
  "description": "Narrative exported to client",
  "minutes_saved": 30,
  "value_usd": 22.5,
  "timestamp": "2026-01-18T20:00:00.000000"
}
```

---

### 3. `POST /api/clients/{client_id}/slack/draft`

Drafts a Slack reply using client context.

**Response:**

```json
{
  "draft": "Here's a draft reply based on the latest client context...",
  "value_event": {
    "client_id": "client_acme",
    "event_type": "slack_draft_reply",
    "description": "Slack reply drafted",
    "minutes_saved": 10,
    "value_usd": 7.5,
    "timestamp": "2026-01-18T20:00:00.000000"
  }
}
```

---

## Updated `/context` Response

Two new fields have been added to the `ContextSnapshot` response:

| Field                   | Type               | Description                                    |
| ----------------------- | ------------------ | ---------------------------------------------- |
| `value_events`          | `List[ValueEvent]` | List of logged system actions for ROI tracking |
| `total_value_generated` | `float`            | Sum of all `value_usd` from events             |

### Full Updated Response Example

```json
{
  "client_id": "client_acme",
  "generated_at": "2026-01-18T20:00:00.000000",
  "headline": "Cash runway at 5.2 months - focus on burn control",
  "alerts": [
    {
      "type": "runway",
      "severity": "high",
      "message": "Cash runway at 5.2 months"
    }
  ],
  "key_metrics": {
    "cash_balance": 4200000.0,
    "monthly_burn": 810000.0,
    "runway_months": 5.2,
    "revenue_mom_growth": 0.06,
    "days_since_last_contact": 7
  },
  "recent_changes": ["AWS spend increased 18% MoM"],
  "open_decisions": [
    {
      "id": "dec_001",
      "question": "Approve Q2 hiring plan?",
      "severity": "high"
    }
  ],
  "last_interaction": {
    "type": "client_call",
    "date": "2026-01-05",
    "summary": "Discussed burn rate and Q1 hiring plan"
  },
  "value_events": [
    {
      "client_id": "client_acme",
      "event_type": "portfolio_refresh",
      "description": "Client context refreshed",
      "minutes_saved": 10,
      "value_usd": 7.5,
      "timestamp": "2026-01-18T20:00:00.000000"
    },
    {
      "client_id": "client_acme",
      "event_type": "narrative_generated",
      "description": "CFO narrative drafted",
      "minutes_saved": 60,
      "value_usd": 45.0,
      "timestamp": "2026-01-18T20:00:00.000000"
    },
    {
      "client_id": "client_acme",
      "event_type": "sentinel_alert",
      "description": "Runway risk detected",
      "minutes_saved": 30,
      "value_usd": 22.5,
      "timestamp": "2026-01-18T20:00:00.000000"
    }
  ],
  "total_value_generated": 75.0
}
```

---

## New TypeScript Types

```typescript
interface ValueEvent {
  client_id: string;
  event_type:
    | "portfolio_refresh"
    | "narrative_generated"
    | "narrative_exported"
    | "sentinel_alert"
    | "slack_draft_reply";
  description: string;
  minutes_saved: number;
  value_usd: number;
  timestamp: string;
}

// Add to existing ContextSnapshot type
interface ContextSnapshot {
  client_id: string;
  generated_at: string;
  headline: string;
  alerts: Alert[];
  key_metrics: KeyMetrics;
  recent_changes: string[];
  open_decisions: OpenDecision[];
  last_interaction: LastInteraction;
  value_events: ValueEvent[]; // NEW
  total_value_generated: number; // NEW
}
```

---

## Event Types & Pricing Reference

| Event Type            | Minutes Saved | Value USD (@ $45/hr) |
| --------------------- | ------------- | -------------------- |
| `portfolio_refresh`   | 10            | $7.50                |
| `narrative_generated` | 60            | $45.00               |
| `narrative_exported`  | 30            | $22.50               |
| `sentinel_alert`      | 30            | $22.50               |
| `slack_draft_reply`   | 10            | $7.50                |

---

## Frontend Implementation Checklist

- [ ] Update `ContextSnapshot` type with `value_events` and `total_value_generated`
- [ ] Add `ValueEvent` type
- [ ] Create "Practice Leverage Dashboard" component to display `total_value_generated`
- [ ] Add value events breakdown UI (loop over `value_events`)
- [ ] Add "Export Narrative" button → `POST /api/clients/{client_id}/export`
- [ ] Add "Draft Slack Reply" button → `POST /api/clients/{client_id}/slack/draft`
- [ ] Optionally add `/roi` endpoint for dedicated ROI view

---

## Notes

- All data remains demo/static for now
- Value tracking is logging-only (no automation)
- CORS works locally out of the box
