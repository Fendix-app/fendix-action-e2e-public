import hashlib


def password_digest(password: str) -> str:
    """Weak hash on a password-shaped variable (fixture for a non-blocking finding)."""
    return hashlib.md5(password.encode()).hexdigest()
