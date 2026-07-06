from services.supabase_service import supabase


def create_business(business_name, email, password):

    response = (
        supabase
        .table("businesses")
        .insert(
            {
                "business_name": business_name,
                "email": email,
                "password": password
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
        .order("created_at", desc=False)
        .execute()
    )

    return response.data