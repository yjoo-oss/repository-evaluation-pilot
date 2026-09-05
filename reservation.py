"""Small authored reservation example for evaluation infrastructure testing."""


def is_active(expires_at: int, now: int) -> bool:
    """Whether the reservation has not reached its exclusive expiry deadline."""
    return now < expires_at
