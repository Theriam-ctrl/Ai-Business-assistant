from services.supabase_service import supabase

from services.analytics_service import (
    get_total_conversations,
    get_most_asked_question
)


def get_dashboard_stats(business_id):
    """
    Returns all dashboard statistics.
    """

    faq_count = (
        supabase
        .table("faqs")
        .select("*", count="exact")
        .eq("business_id", business_id)
        .execute()
    )

    lead_count = (
        supabase
        .table("leads")
        .select("*", count="exact")
        .eq("business_id", business_id)
        .execute()
    )

    return {
        "faqs": faq_count.count or 0,
        "leads": lead_count.count or 0,
        "conversations": get_total_conversations(business_id),
        "most_asked": get_most_asked_question(business_id)
    }


def get_recent_leads(business_id, limit=5):

    response = (
        supabase
        .table("leads")
        .select("*")
        .eq("business_id", business_id)
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )

    return response.data


def get_recent_conversations(business_id, limit=5):
    """
    Returns the most recent conversations.
    """

    response = (
        supabase
        .table("conversations")
        .select("*")
        .eq("business_id", business_id)
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )

    return response.data