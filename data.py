from typing import List, Dict, Any, Optional, Union
from enum import Enum

class OpcoesStatus(str, Enum):
    a_fazer = "A Fazer"
    fazendo = "fazendo"
    feito = "feito"

Item = Dict[str, Union[int, str, OpcoesStatus]]


class TodoData:
    todo: List[Item] = [{
        "id": 1, 
        "titulo": "Fazer live", 
        "descricao": "Fazer live na casa do caraio", 
        "status": OpcoesStatus.fazendo
    },
        {"id": 2, 
        "titulo": "Ligar Streaming cu", 
        "descricao": "Fazer live logo", 
        "status": OpcoesStatus.a_fazer}]

    id_atual = 2

    

    def listar(self):
        return self.todo

    def inserir(self, item: Item) -> Item :
         self.id_atual += 1
         item["id"] = self.id_atual
         self.todo.append(item)
         return item
        
    def pegar(self, item_id: int) -> Item:
        item = filter(lambda x: x["id"] == item_id, self.todo)
        return list(item)[0]
