"""
Prompt templates for incident summarization.
"""


def build_summary_prompt(incident: dict) -> str:
    """
    Build a prompt for generating an incident summary.
    """

    return f"""
You are an experienced IT Incident Management Assistant.

Your task is to generate a concise and professional summary of the following incident.

Incident Details

Incident ID:
{incident.get("incident_id", "N/A")}

Priority:
{incident.get("priority", "N/A")}

Category:
{incident.get("category", "N/A")}

Short Description:
{incident.get("short_description", "N/A")}

Description:
{incident.get("description", "N/A")}

Instructions:

- Keep the summary under 80 words.
- Use professional language.
- Do not invent information.
- Base the summary only on the provided incident details.
- Return only the summary without bullet points or headings.
"""