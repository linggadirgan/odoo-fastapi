from fastapi import APIRouter, HTTPException, Depends
from app.schemas.odoo_schemas import WasteRecordSchema
from app.services.odoo_client import connect_odoo
from app.core.logger import logger
from app.utils.response_handler import success_response, notfound_response, error_response

router = APIRouter()

@router.post('/waste-record-list/')
def waste_record_list(params: WasteRecordSchema, odoo=Depends(connect_odoo)):
    try:
        response = odoo['waste.record'].waste_record_list(params.dict())
        if response and response.get('data', False):
            return success_response(data=response)
        else:
            return notfound_response(data=response)
    except Exception as e:
        error_response(message=str(e))