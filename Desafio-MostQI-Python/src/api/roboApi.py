from fastapi import FastAPI
from typing import Optional
from service.roboService import searchData

app = FastAPI()

@app.get("/robo/{cpf}")
async def getResources(cpf: str, nome: Optional[str] = None, nis: Optional[str] = None,
                       beneficiario: bool = False):
    return searchData(cpf=cpf, nome=nome, nis=nis, beneficiario=beneficiario)