import json
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_faqs(knowledge):
    """
    Generates 20 FAQs from structured business knowledge.
    Returns a Python list of dictionaries.
    """

    prompt = f"""
You are an expert customer support consultant.

Using the business information below, generate the 20 most common customer questions.

Rules:

- Return EXACTLY 20 FAQs.
- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT explain anything.
- Do NOT include text before or after the JSON.
- Every FAQ must contain:
    - question
    - answer

Return this exact structure:

[
    {{
        "question": "",
        "answer": ""
    }}
]

Business Knowledge:

{json.dumps(knowledge, indent=2)}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.2,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown if the AI adds it
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    # Extract JSON array
    start = content.find("[")
    end = content.rfind("]") + 1

    if start == -1 or end == 0:

        raise Exception(
            f"AI returned invalid FAQ JSON:\n\n{content}"
        )

    json_text = content[start:end]

    try:

        faqs = json.loads(json_text)

    except json.JSONDecodeError as e:

        raise Exception(
            f"""
FAQ JSON Parse Error

{e}

Returned by AI:

{content}
"""
        )

    return faqs