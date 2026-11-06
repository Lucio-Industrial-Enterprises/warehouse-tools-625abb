"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse an integer quantity, rejecting negative values."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return quantity
