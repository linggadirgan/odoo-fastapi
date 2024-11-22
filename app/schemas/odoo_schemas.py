from pydantic import BaseModel
from typing import Optional,List

class WasteRecordSchema(BaseModel):
    name: Optional[str]
    production_id: Optional[str]
    state: Optional[str]
    waste_type_id: Optional[int]
    user_id: Optional[int]