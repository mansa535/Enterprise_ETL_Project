from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class Customer(BaseModel):
    model_config = ConfigDict(extra="ignore")

    external_id: str
    source: str
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    website: str | None = None
    industry: str | None = None
    created_at: datetime | None = None