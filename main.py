from fastapi import FastAPI
from typing import List, Dict, Any, Optional
from data import TodoData
from modelos import ItemModel, ItemModelResponse

todo = TodoData()
app = FastAPI()


@app.get("/todo", response_model=List[ItemModelResponse])
def litar_to_do():
    """
    view que retorna lista to do
    """
    return todo.listar()


@app.post("/todo", response_model=ItemModelResponse)
def inserir_to_do(item_a_inserir: ItemModel):
    """
insere item na lista todo
    """
    return todo.inserir(item_a_inserir.dict())

@app.get("/todo/{id_item}", response_model=ItemModelResponse)
def pegar_item(item_id: int):
    """
pega item na lista todo
    """
    return todo.pegar(item_id)


