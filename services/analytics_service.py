import json


def get_conversations():

    with open("data/conversations.json", "r") as file:
        return json.load(file)


def save_conversation(question, answer):

    conversations = get_conversations()

    conversations.append(
        {
            "question": question,
            "answer": answer
        }
    )

    with open("data/conversations.json", "w") as file:
        json.dump(
            conversations,
            file,
            indent=4
        )


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