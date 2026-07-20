from services.supabase_service import supabase


def create_business(
    user_id,
    business_name,
    owner_name,
    email,
    phone=""
):
    """
    Creates a new business after successful registration.
    """

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
                "slug": slug,

                # Onboarding
                "industry": "",
                "setup_step": 1,
                "onboarding_complete": False
            }
        )
        .execute()
    )

    return response


def get_all_businesses():
    """
    Returns every registered business.
    """

    response = (
        supabase
        .table("businesses")
        .select("*")
        .order("created_at")
        .execute()
    )

    return response.data


def get_business_by_user(user_id):
    """
    Returns the business belonging to the logged-in user.
    """

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
    """
    Used by the public receptionist.
    """

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
    """
    Updates the business profile.
    """

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


def update_business_logo(
    business_id,
    logo_url
):
    """
    Updates the business logo.
    """

    response = (
        supabase
        .table("businesses")
        .update(
            {
                "logo": logo_url
            }
        )
        .eq("id", business_id)
        .execute()
    )

    return response


def complete_onboarding(
    business_id,
    industry,
    welcome_message,
    ai_personality
):
    """
    Marks onboarding as complete.
    """

    response = (
        supabase
        .table("businesses")
        .update(
            {
                "industry": industry,
                "welcome_message": welcome_message,
                "ai_personality": ai_personality,
                "setup_step": 6,
                "onboarding_complete": True
            }
        )
        .eq("id", business_id)
        .execute()
    )

    return response