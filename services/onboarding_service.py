from services.supabase_service import supabase


def update_onboarding(
    business_id,
    industry,
    ai_personality,
    welcome_message
):

    response = (
        supabase
        .table("businesses")
        .update(
            {
                "industry": industry,
                "ai_personality": ai_personality,
                "welcome_message": welcome_message,
                "onboarding_complete": True,
                "setup_step": 6
            }
        )
        .eq("id", business_id)
        .execute()
    )

    return response