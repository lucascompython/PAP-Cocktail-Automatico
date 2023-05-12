import math
from time import sleep

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pins import enviar_armazenamento_para_o_automato, mover_eixo, run_motores

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@app.get("/get_percentages")
def get_percentages() -> dict[str, list[int]]:

    return enviar_armazenamento_para_o_automato(just_percentages=True)

@app.post("/start")
def start(liquido1: int, liquido2: int, liquido3: int): 
    voltas1 = math.ceil((liquido1 / 0.000167) / 1000)
    voltas2 = math.ceil((liquido2 / 0.000167) / 1000)
    voltas3 = math.ceil((liquido3 / 0.000167) / 1000)

    mover_eixo(1)
    sleep(2) # dar tempo para o eixo se mover
    run_motores(voltas1, 1)
    sleep(50) 

    mover_eixo(2)
    sleep(2) # dar tempo para o eixo se mover
    run_motores(voltas2, 2)
    sleep(50) 

    mover_eixo(3)
    sleep(2) # dar tempo para o eixo se mover
    run_motores(voltas3, 3)
    sleep(50)

    mover_eixo(4) # retorno
    sleep(2) # dar tempo para o eixo se mover

    return {"status": "ok"}


