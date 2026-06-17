import json


def load_faqs():

    with open("data/faq_data.json", "r") as file:
        return json.load(file)


def build_faq_context(faq_data):

    return "\n".join(
        [
            f"Question: {item['question']}\nAnswer: {item['answer']}"
            for item in faq_data
        ]
    )


def add_faq(question, answer):

    with open("data/faq_data.json", "r") as file:
        faqs = json.load(file)

    faqs.append(
        {
            "question": question,
            "answer": answer
        }
    )

    with open("data/faq_data.json", "w") as file:
        json.dump(faqs, file, indent=4)


def delete_faq(index):

    with open("data/faq_data.json", "r") as file:
        faqs = json.load(file)

    faqs.pop(index)

    with open("data/faq_data.json", "w") as file:
        json.dump(faqs, file, indent=4)


def update_faq(index, question, answer):

    with open("data/faq_data.json", "r") as file:
        faqs = json.load(file)

    faqs[index] = {
        "question": question,
        "answer": answer
    }

    with open("data/faq_data.json", "w") as file:
        json.dump(faqs, file, indent=4)