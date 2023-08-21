from fastapi import FastAPI
from rutas import router


app = FastAPI(title='API Json',
              description='API to query database tables and returns it in Json format',
              version='1'
              )
app.include_router(router)