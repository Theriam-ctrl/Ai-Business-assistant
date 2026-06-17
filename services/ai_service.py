from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(user_question, faq_context):

    system_prompt = f"""
You are a professional customer support assistant.

Answer questions ONLY using the information below.

If the information is unavailable, reply:

'I do not have that information yet. Please contact the business directly.'

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