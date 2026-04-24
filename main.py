from fastapi import FastAPI
from api.rutas import principal


app=FastAPI()
app.include_router(principal.router)


