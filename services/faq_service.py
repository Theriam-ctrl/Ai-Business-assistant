from services.supabase_service import supabase


def load_faqs(business_id):

    response = (
        supabase
        .table("faqs")
        .select("*")
        .eq("business_id", business_id)
        .order("created_at")
        .execute()
    )

    return response.data


def build_faq_context(faq_data):

    return "\n".join(
        [
            f"Question: {item['question']}\nAnswer: {item['answer']}"
            for item in faq_data
        ]
    )


def add_faq(
    business_id,
    question,
    answer
):

    response = (
        supabase
        .table("faqs")
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


def delete_faq(faq_id):

    response = (
        supabase
        .table("faqs")
        .delete()
        .eq("id", faq_id)
        .execute()
    )

    return response


def update_faq(
    faq_id,
    question,
    answer
):

    response = (
        supabase
        .table("faqs")
        .update(
            {
                "question": question,
                "answer": answer
            }
        )
        .eq("id", faq_id)
        .execute()
    )

    return response