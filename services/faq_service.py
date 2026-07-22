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

    return (
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


def update_faq(
    faq_id,
    question,
    answer
):

    return (
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


def delete_faq(faq_id):

    return (
        supabase
        .table("faqs")
        .delete()
        .eq("id", faq_id)
        .execute()
    )


def delete_all_faqs(
    business_id
):

    return (
        supabase
        .table("faqs")
        .delete()
        .eq(
            "business_id",
            business_id
        )
        .execute()
    )