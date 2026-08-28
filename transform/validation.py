from pydantic import ValidationError
from load.models import Customer


def validate_customer(record: dict) -> Customer | None:
    """
    Validate a transformed customer record using the Customer model.
    """

    try:
        return Customer(**record)

    except ValidationError as e:
        print(f"Validation failed: {e}")
        return None