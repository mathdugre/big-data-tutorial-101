"""Minimal function to demonstrate pytest."""


def greet(username: str | None = None) -> str:
    """Greet a given user.

    When no user is given, this function will return "Hello World!".

    Parameters
    ----------
    username: Optional[str]
        Name of the user.

    Returns
    -------
    str
        Personalized greeting.
    """
    username = username if username else "World"
    return f"Hello {username}!"
