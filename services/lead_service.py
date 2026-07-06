from services.supabase_service import supabase


def get_all_leads():

    response = (
        supabase
        .table("leads")
        .select("*")
        .order("created_at", desc=False)
        .execute()
    )

    return response.data


def save_lead(name, phone):

    response = (
        supabase
        .table("leads")
        .insert(
            {
                "name": name,
                "phone": phone
            }
        )
        .execute()
    )

    return response