from services.supabase_service import supabase


def get_business_leads(business_id):

    response = (
        supabase
        .table("leads")
        .select("*")
        .eq("business_id", business_id)
        .order("created_at", desc=False)
        .execute()
    )

    return response.data


def save_lead(business_id, name, phone):

    response = (
        supabase
        .table("leads")
        .insert(
            {
                "business_id": business_id,
                "name": name,
                "phone": phone
            }
        )
        .execute()
    )

    return response