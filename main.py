from fastapi import FastAPI
from info_rede import get_status_rede

app = FastAPI()

@app.get("/")
async def get_status_ping():
    status_ping = get_status_rede.retorna_status_ping()
    return status_ping
