from collections import Counter
from datetime import datetime, timedelta

from services.supabase_service import supabase


def get_conversations(business_id):

    response = (
        supabase
        .table("conversations")
        .select("*")
        .eq("business_id", business_id)
        .order("created_at", desc=False)
        .execute()
    )

    return response.data


def save_conversation(business_id, question, answer):

    response = (
        supabase
        .table("conversations")
        .insert(
            {
                "business_id": business_id,
                "question": question,
                "answer": answer
            }
        )
        .execute()
    )

    return response


def get_total_conversations(business_id):

    response = (
        supabase
        .table("conversations")
        .select("*", count="exact")
        .eq("business_id", business_id)
        .execute()
    )

    return response.count or 0


def get_most_asked_question(business_id):

    conversations = get_conversations(business_id)

    if not conversations:
        return "No conversations yet"

    questions = Counter()

    for conversation in conversations:
        questions[conversation["question"]] += 1

    return questions.most_common(1)[0][0]


def get_weekly_conversations(business_id):
    """
    Returns the number of conversations
    for each of the last 7 days.
    """

    conversations = get_conversations(business_id)

    today = datetime.utcnow().date()

    results = {}

    for i in range(6, -1, -1):

        day = today - timedelta(days=i)

        results[day.strftime("%a")] = 0

    for conversation in conversations:

        created = datetime.fromisoformat(
            conversation["created_at"].replace("Z", "+00:00")
        ).date()

        label = created.strftime("%a")

        if label in results:
            results[label] += 1

    return results