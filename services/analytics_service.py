from services.supabase_service import supabase


def get_conversations():

    response = (
        supabase
        .table("conversations")
        .select("*")
        .order("created_at", desc=False)
        .execute()
    )

    return response.data


def save_conversation(question, answer):


    response = (
        supabase
        .table("conversations")
        .insert(
            {
                "question": question,
                "answer": answer
            }
        )
        .execute()
    )



    return response


def get_most_asked_question():

    conversations = get_conversations()

    if not conversations:
        return "No conversations yet"

    questions = {}

    for conversation in conversations:

        question = conversation["question"]

        if question in questions:
            questions[question] += 1
        else:
            questions[question] = 1

    return max(
        questions,
        key=questions.get
    )