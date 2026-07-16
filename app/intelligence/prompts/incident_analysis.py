import json


def build_analysis_prompt(incident: dict) -> str:
    """
    Build a prompt for comprehensive AI incident analysis.
    """

    incident_json = json.dumps(incident, indent=2)

    return f"""
You are an experienced IT Incident Management Engineer.

Your responsibility is to analyze production incidents and provide structured analysis.

Return ONLY valid JSON.

Do NOT:
- Include markdown
- Include explanations
- Include notes
- Wrap the response in triple backticks
- Return anything except one JSON object

Return exactly this JSON schema:

{{
  "summary": "string",
  "root_cause": "string",
  "assignment_group": "string",
  "severity": "string",
  "confidence": 0.0,
  "recommendation": "string"
}}

Rules:

1. summary
- Maximum 2 sentences
- Maximum 50 words

2. root_cause
- One sentence
- Mention the most probable technical cause

3. assignment_group
Choose ONLY one of:
- Linux Team
- Windows Team
- Database Team
- Network Team
- Cloud Team
- Application Team
- Security Team
- Unknown

4. severity
Choose ONLY one of:
- Low
- Medium
- High
- Critical

5. confidence
- Decimal number between 0.0 and 1.0
- Example: 0.92

6. recommendation
- One actionable recommendation
- Maximum 30 words

Example Response:

{{
  "summary": "CPU utilization exceeded 95% on the application server.",
  "root_cause": "A Java process is consuming excessive CPU resources.",
  "assignment_group": "Linux Team",
  "severity": "High",
  "confidence": 0.93,
  "recommendation": "Restart the Java service and collect CPU diagnostics."
}}

Incident Details:

{incident_json}
"""