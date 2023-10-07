import os

from dotenv import load_dotenv
from fastapi_users.authentication import (CookieTransport,
                                          JWTStrategy,
                                          AuthenticationBackend)


load_dotenv()

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)


SECRET = os.getenv("SECRET")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
