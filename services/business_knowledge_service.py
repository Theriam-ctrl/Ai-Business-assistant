from services.supabase_service import supabase


def save_business_knowledge(
    business_id,
    knowledge
):
    print("Knowledge type:", type(knowledge))
    print("Knowledge value:", knowledge)

    response = (
        supabase
        .table("business_knowledge")
        .upsert(
            {
                "business_id": business_id,
                "business_name": knowledge.get(
                    "business_name",
                    ""
                ),
                "industry": knowledge.get(
                    "industry",
                    ""
                ),
                "description": knowledge.get(
                    "description",
                    ""
                ),
                "target_customers": knowledge.get(
                    "target_customers",
                    ""
                ),
                "tone": knowledge.get(
                    "tone",
                    ""
                ),
                "services": knowledge.get(
                    "services",
                    []
                )
            }
        )
        .execute()
    )

    return response


def get_business_knowledge(
    business_id
):

    response = (
        supabase
        .table("business_knowledge")
        .select("*")
        .eq(
            "business_id",
            business_id
        )
        .limit(1)
        .execute()
    )

    if response.data:

        return response.data[0]

    return None