from typing import Any


def map_customer_record(record: dict[str, Any], source: str) -> dict[str, Any]:
    """
    Map a source-specific customer record into the unified customer schema.
    """

    if source.lower() == "stripe":
        return {
            "external_id": record.get("id"),
            "name": record.get("name"),
            "email": record.get("email"),
            "phone": record.get("phone"),
            "source": "stripe",
        }

    if source.lower() == "salesforce":
        return {
            "external_id": record.get("Id"),
            "name": record.get("Name"),
            "email": record.get("Email"),
            "phone": record.get("Phone"),
            "source": "salesforce",
        }

    raise ValueError(f"Unsupported source: {source}")