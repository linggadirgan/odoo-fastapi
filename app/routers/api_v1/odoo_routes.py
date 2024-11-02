from fastapi import APIRouter, Depends, HTTPException
from app.schemas.odoo_schemas import OdooRequestSchema
from app.services.odoo_client import OdooClient
from app.core.logger import logger

logger.info("This is an informational message.")
logger.error("This is an error message.")

router = APIRouter()

@router.post("/get_records/")
async def get_records(request: OdooRequestSchema):
    client = OdooClient()
    response = client.get_records(request.model, request.fields, request.domain)
    if response:
        return response
    raise HTTPException(status_code=404, detail="No records found")
