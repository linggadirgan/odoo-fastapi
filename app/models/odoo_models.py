from pydantic import BaseModel
from typing import Optional

class OdooRecord(BaseModel):
    id: int
    name: str
    description: Optional[str]
