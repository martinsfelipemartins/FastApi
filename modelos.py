from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from data import OpcoesStatus

class ItemModel(BaseModel):
     
    titulo: str
    descricao: str
    status: OpcoesStatus

class ItemModelResponse(ItemModel):
    id: int
