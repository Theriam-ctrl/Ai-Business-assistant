import json
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyse_business(text):
    """
    Analyses a business website and returns structured business knowledge.
    """

    prompt = f"""
You are an expert business analyst.

Analyse the business website below and return ONLY a valid JSON object.

Rules:
- Do not use markdown.
- Do not use ```json.
- Do not explain anything.
- Do not include any text before or after the JSON.
- If you are unsure about a field, return an empty string.
- The services field MUST always be an array.

Return this exact structure:

{{
    "business_name": "",
    "industry": "",
    "description": "",
    "services": [],
    "target_customers": "",
    "tone": ""
}}

Website Content:

{text[:15000]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()
    print("\n================ AI RESPONSE ================\n")
    print(content)
    print("\n=============================================\n")
    # Remove markdown code blocks if present
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    # Extract JSON if the AI added extra text
    start = content.find("{")
    end = content.rfind("}") + 1

    if start == -1 or end == 0:
        raise Exception(
            f"AI did not return valid JSON.\n\nReturned:\n{content}"
        )

    json_text = content[start:end]

    try:
        knowledge = json.loads(json_text)

    except json.JSONDecodeError as e:

        raise Exception(
            f"""
JSON Parse Error

{e}

Returned by AI:

{content}
"""
        )

    # Ensure every expected field exists
    knowledge.setdefault("business_name", "")
    knowledge.setdefault("industry", "")
    knowledge.setdefault("description", "")
    knowledge.setdefault("services", [])
    knowledge.setdefault("target_customers", "")
    knowledge.setdefault("tone", "")

    # Make sure services is always a list
    if not isinstance(knowledge["services"], list):
        knowledge["services"] = []

    return knowledge