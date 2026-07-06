from services.supabase_service import supabase

response = (
    supabase
    .table("conversations")
    .insert(
        {
            "question": "Test Question",
            "answer": "Test Answer"
        }
    )
    .execute()
)

print(response)