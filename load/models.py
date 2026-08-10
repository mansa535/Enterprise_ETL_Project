from pydantic import BaseModel, EmailStr
from typing import Optional


class Customer(BaseModel):
    id: str
    name: Optional[str] = None
    email: Optional[EmailStr] = None