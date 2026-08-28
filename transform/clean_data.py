import re
from typing import Any


def clean_string(value: Any) -> str | None:
    if value is None:
        return None

    value = str(value).strip()

    if not value:
        return None

    return value


def clean_email(value: Any) -> str | None:
    value = clean_string(value)

    if value is None:
        return None

    return value.lower()


def clean_phone(value: Any) -> str | None:
    value = clean_string(value)

    if value is None:
        return None

    return re.sub(r"[^\d+]", "", value)


def clean_customer_record(record: dict) -> dict:
    return {
        "external_id": clean_string(
            record.get("external_id") or record.get("Id")
        ),
        "name": clean_string(
            record.get("name") or record.get("Name")
        ),
        "email": clean_email(
            record.get("email") or record.get("Email")
        ),
        "phone": clean_phone(
            record.get("phone") or record.get("Phone")
        ),
        "source": clean_string(record.get("source")),
    }