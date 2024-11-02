from pydantic import BaseModel
from typing import Optional

class OdooRequestSchema(BaseModel):
    model: str
    fields: list[str]
    domain: Optional[list] = []

class OdooResponseSchema(BaseModel):
    id: int
    name: str
    additional_info: Optional[str]
