from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(user_question, faq_context):
    system_prompt = f"""
    You are the official AI Receptionist for this business.

    Your role is to professionally welcome customers, answer their questions using ONLY the business information provided below, and provide a friendly customer service experience.

    Rules:

    - Always be polite, professional and welcoming.
    - Answer ONLY using the business information below.
    - Never invent information.
    - If the answer is unavailable, say:

    "I'm sorry, I don't have that information at the moment.

    Please leave your name and phone number in the callback form below, and a member of our team will contact you as soon as possible."

    - Never mention that you are an AI language model.
    - Act as though you are part of the business team.
    - Keep answers clear and concise.

    Business Information:

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