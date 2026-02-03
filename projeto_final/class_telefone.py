
from class_produto import Produto 

class Telefone(Produto):

    def __init__(self, nome: str, descricao: str, quantidade: int, custo: float, telefones_quebrados: int)-> None:

        super().__init__(nome, descricao, quantidade, custo) 

        assert telefones_quebrados >= 0, "Não pode haver menos de 0 telefones quebrados."

        # Criamos um objeto produto e especializamos na classe filha. 

        self.__telefones_quebrados = telefones_quebrados

