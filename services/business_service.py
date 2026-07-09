from services.supabase_service import supabase


def create_business(
    user_id,
    business_name,
    owner_name,
    email,
    phone=""
):

    response = (
        supabase
        .table("businesses")
        .insert(
            {
                "user_id": user_id,
                "business_name": business_name,
                "owner_name": owner_name,
                "email": email,
                "phone": phone
            }
        )
        .execute()
    )

    return response


def get_all_businesses():

    response = (
        supabase
        .table("businesses")
        .select("*")
        .order("created_at")
        .execute()
    )

    return response.data
def get_business_by_user(user_id):

    response = (
        supabase
        .table("businesses")
        .select("*")
        .eq("user_id", user_id)
        .single()
        .execute()
    )

    return response.data