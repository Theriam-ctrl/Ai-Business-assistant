from services.supabase_service import supabase


def create_business(
    user_id,
    business_name,
    owner_name,
    email,
    phone=""
):

    slug = (
        business_name
        .lower()
        .strip()
        .replace(" ", "-")
    )

    response = (
        supabase
        .table("businesses")
        .insert(
            {
                "user_id": user_id,
                "business_name": business_name,
                "owner_name": owner_name,
                "email": email,
                "phone": phone,
                "welcome_message": "",
                "ai_personality": "Professional",
                "slug": slug
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


def get_business_by_slug(slug):

    response = (
        supabase
        .table("businesses")
        .select("*")
        .eq("slug", slug)
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def update_business(
    business_id,
    business_name,
    owner_name,
    phone,
    welcome_message,
    ai_personality
):

    slug = (
        business_name
        .lower()
        .strip()
        .replace(" ", "-")
    )

    response = (
        supabase
        .table("businesses")
        .update(
            {
                "business_name": business_name,
                "owner_name": owner_name,
                "phone": phone,
                "welcome_message": welcome_message,
                "ai_personality": ai_personality,
                "slug": slug
            }
        )
        .eq("id", business_id)
        .execute()
    )

    return response