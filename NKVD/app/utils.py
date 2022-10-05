import jwt


def get_headers(token: str) -> dict:
    return jwt.get_unverified_header(token)
