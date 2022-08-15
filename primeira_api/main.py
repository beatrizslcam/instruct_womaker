import json
from sys import float_repr_style
from typing import Optional, Union
from fastapi import FastAPI, Header
from pydantic import BaseModel #para pegar o conteúdo do body
#para rodar usar uvicorn main:app --reload

class Item(BaseModel):
    id: int
    quantidade: int
    valor: float

banco= []

app = FastAPI()

#endpoints se refere a duas pontas que estão se comunicando por protocolos através da troca de dados
#get = pegar, pot: enviar
@app.get("/listar_itens")
def listar_itens():
    return banco
    
#leitura do header: Quando é legal: para tokens,logins, etc
# @app.post("/")
#def read_root(user_agent: Optional [str] = Header(None)): 
#    return {"user_agent": user_agent}

@app.post("/add_item")
def add_item(novo_item: Item):
    banco.append(novo_item)
    return print(f'item adicionado com sucesso: {novo_item}')


@app.get("/item/valor_total")
def get_valor_total(): 
    valor_total = 0.0
    for item in banco:
        valor_total+=item.valor*item.quantidade
    return valor_total


@app.delete('/remover_item/{id}')
def remover_item(id):
    for item in banco:
        if(item.id == id):
            banco.remove(id)
            return print("O item foi removido com sucesso")
        else:
            return print("Item não identificado")
    
