⸻

CFO Context Backend

Demo Backend for CFO Pre-Call Context

This backend provides CFO-ready context snapshots for clients. It is a
lightweight FastAPI service that generates pre-call insights, alerts,
metrics, and open xdecisions for a client.

⸻

API

Get Client Context

GET /api/clients/{client_id}/context

Parameters: • client_id (string): ID of the client, e.g., client_acme.

Response:

{ "client_id": "client_acme", "generated_at":
"2026-01-12T23:39:49.943321", "headline": "Cash runway at 5.2 months ---
focus on burn control before growth", "alerts": \[ { "type": "runway",
"severity": "high", "message": "Cash runway at 5.2 months" } \],
"key_metrics": { "cash_balance": 4200000.0, "monthly_burn": 810000.0,
"runway_months": 5.2, "revenue_mom_growth": 0.06,
"days_since_last_contact": 7.0, "aws_spend": 50000.0, "payroll":
500000.0, "marketing": 75000.0 }, "recent_changes": \[ "Cash balance
changed from 4000000.0 to 4200000.0 (5.0% MoM)", "Monthly burn changed
from 750000.0 to 810000.0 (8.0% MoM)", "... more changes ..." \],
"open_decisions": \[ { "id": "dec_001", "question": "Approve Q2 hiring
plan?", "severity": "high" } \], "last_interaction": { "type":
"client_call", "date": "2026-01-05", "summary": "Discussed burn rate and
Q1 hiring plan" } }

⸻

Local Demo

You can run a quick test locally:

# Activate virtual environment

source .venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run the FastAPI backend

uvicorn main:app --reload

Then, in Python or Postman, you can do:

from app.context.builder import build_context_snapshot

snapshot = build_context_snapshot("client_acme")
print(snapshot.model_dump_json(indent=2))

⸻

Frontend Integration Notes • Endpoint: /api/clients/{client_id}/context
• Returns full snapshot in JSON format. • Frontend can use generated_at
for timestamps, headline for display, alerts and key_metrics for
dashboard widgets, recent_changes for highlighting changes,
open_decisions for actionable items, and last_interaction for call prep.

Example Usage (JS/React):

const res = await
fetch(`https://your-backend.com/api/clients/client_acme/context`); const
data = await res.json(); console.log(data.headline); // Display headline

⸻

What's Included • main.py -- FastAPI entry point •
app/context/builder.py -- Core logic generating context snapshots •
demo_client.py -- Simple Python client to test API • Documentation here
in README for integration

⸻

Next Steps for Igwe (Frontend) 1. Clone the repo:

git clone https://github.com/Kdhungel/cfo-context-backend-.git

    2.  Start backend locally or on a dev server.
    3.  Consume /api/clients/{client_id}/context endpoint in frontend.
    4.  Reference the frontend integration section for how JSON is structured.

⸻
