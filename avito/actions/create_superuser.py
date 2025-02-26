import asyncio
import contextlib
from os import getenv

from api.dependencies.authentification.user_manager import get_user_manager
from api.dependencies.authentification.users import get_users_db
from core.authentication.user_manager import UserManager
from core.models import db_helper, User
from schemas.user import UserCreate


# get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


default_username = getenv("DEFAULT_USERNAME", "unknown")
default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "abc")
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        # safe=False,
    )
    return user


async def create_superuser(
    username: str = default_username,
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        username=username,
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                existing_user = await user_manager.get_by_username(username)
                if existing_user:
                    print(f"Пользователь с username '{username}' уже существует.")
                    return existing_user

                # Если пользователя нет, создаем нового
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
