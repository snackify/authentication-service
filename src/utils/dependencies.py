from .hash_password import HashPassword


async def get_hash_password() -> HashPassword:
    return HashPassword()
