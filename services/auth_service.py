from services.supabase_service import supabase


def register_user(email, password):

    return supabase.auth.sign_up(
        {
            "email": email,
            "password": password
        }
    )


def login_user(email, password):

    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password
        }
    )

    print("\n========== SESSION ==========")

    session = supabase.auth.get_session()

    print(session)

    print("=============================\n")

    return response


def logout_user():

    supabase.auth.sign_out()