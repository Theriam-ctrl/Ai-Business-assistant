import uuid

from services.supabase_service import supabase


def upload_logo(file, slug):

    extension = file.name.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    path = f"{slug}/{filename}"

    supabase.storage.from_("logos").upload(
        path,
        file.getvalue()
    )

    public_url = (
        supabase
        .storage
        .from_("logos")
        .get_public_url(path)
    )

    return public_url