from pydantic import BaseModel, validator
from datetime import datetime
# from typing import dict


class Parameters(BaseModel):
    InitalDate: str
    EndDate: str
    CenterId: int
    Querytype: int

    @validator('QueryType')
    def Querytype_Validate(cls, Querytype):
        
        if Querytype == 1:
            return 'query_1.sql'
        if Querytype == 2:
            return 'query_2.sql'
        else:
            return 'invalid query'

    @validator('InitalDate')
    def InitalDate_validate(cls, InitalDate):
        if datetime.strptime(InitalDate, '%Y-%m-%d'):
            return InitalDate
        else:
            raise ValueError('Formato de fecha: formato de fecha incorrecto')

    @validator('EndDate')
    def EndDate_validate(cls, EndDate):
        if datetime.strptime(EndDate, '%Y-%m-%d'):
            return EndDate
        else:
            raise ValueError('Formato de fecha: formato de fecha incorrecto')

    class Config:
        schema_extra = {
            "example": {
                'InitalDate': '2021-11-01',
                'EndDate': '2021-11-015',
                'CenterId': 1,
                'Querytype': 1
            }
        }


class Response200(BaseModel):
    data: dict
    prev_page: int
    next_page: int


class Error(BaseModel):
    message: str