from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Parameters, Response200, Error
from connection import Connection
import json
router = APIRouter()

responses = {404: {"model": Error,
                   "description": "Item not found",
                   "content": {"application/json": {
                       "example": {
                           "message": "Item not found"}}}}}


@ router.post('/', responses={**responses}, response_model=Response200)
def obtener_turnos_get(model: Parameters):

    request = json.loads(Connection(
        model.InitalDate, model.EndDate, model.CenterId, model.Querytype))
    print(type(request))
    print(len(request))

    if request:
        return {
            'data': request,
            'prev_page': 1,
            'next_page': 3
        }
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})