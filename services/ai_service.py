from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(
    user_question,
    business,
    faq_context
):

    welcome_message = (
        business.get("welcome_message")
        or "Welcome!"
    )

    personality = (
        business.get("ai_personality")
        or "Professional"
    )

    business_name = business["business_name"]

    system_prompt = f"""
You are the official AI Receptionist for {business_name}.

Business Welcome Message:
{welcome_message}

AI Personality:
{personality}

Your responsibilities:

- Welcome customers warmly.
- Answer ONLY using the business knowledge below.
- Never invent information.
- If the information is unavailable, say:

"I'm sorry, I don't have that information at the moment.

Please leave your name and phone number in the callback form below and a member of our team will contact you."

- Never mention you are an AI language model.
- Act as a real member of the business.
- Keep responses concise.

Business Knowledge:

{faq_context}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    return response.choices[0].message.content