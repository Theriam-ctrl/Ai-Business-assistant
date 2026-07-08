from services.supabase_service import supabase


def register_user(email, password):

    response = supabase.auth.sign_up(
        {
            "email": email,
            "password": password
        }
    )

    return response


def login_user(email, password):

    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password
        }
    )

    return response


def logout_user():

    supabase.auth.sign_out()