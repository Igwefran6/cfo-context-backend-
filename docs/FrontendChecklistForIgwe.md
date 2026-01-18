## Frontend Contract Checklist – Value Audit

1. **Endpoint:** `/api/clients/{client_id}/value-audit`
   - GET request
   - Returns JSON with:
     - `client_id` (string)
     - `total_value_generated` (float)
     - `value_events` (list of dicts)
     - `summary` (string)
     
2. **Integration Notes**
   - Can be displayed in a “Practice Leverage Dashboard” widget
   - Use `total_value_generated` as main KPI
   - Loop over `value_events` to show task type, minutes saved, and value USD
   - `summary` provides human-friendly sentence for display
     
3. **Frontend UI Suggestions**
   - Small card or modal showing:
     - Total dollars saved
     - Breakdown by type (portfolio refresh, narrative generated, alerts)
   - Optional: hover-over for each event timestamp
     
4. **Testing**
   - Ensure GET request returns proper JSON for demo client (`client_acme`)
   - Validate `total_value_generated` equals sum of `value_usd` in `value_events`
   - Confirm summary matches the number of events and total value