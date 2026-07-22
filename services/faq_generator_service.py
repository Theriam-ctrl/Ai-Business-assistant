import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_faqs(knowledge):

    prompt = f"""
You are creating FAQs for an AI Receptionist.

Using the business information below, generate 20 frequently asked questions.

Requirements:

- Return exactly 20 FAQs.
- Each FAQ must have:
  Question:
  Answer:

- Questions should be realistic.
- Answers should be professional.
- Do not invent information that is not supported by the business description.
- Use a friendly business tone.

Business Information:

{knowledge}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content