# Encapsulamento - Uma forma de proteger os nossos atributos de acessos indevidos, limitando a leitura 
# e a escrita, o bem conhecido getters e setters. 

from __future__ import annotations 
from typing import List 


class Produto:

    todos_produtos: List[Produto] = []

    def __init__(self, nome: str= "", quantidade: int= 0, custo: float= 0, preco: float= 0)-> None:

        # Atributos privados 

        self.__nome = nome 
        self.__quantidade = quantidade 
        self.__custo = custo 
        self.__preco = preco 

        Produto.todos_produtos.append(self)

    # Definindo os getters e os setters 
    # Ditando de que forma os nossos atributos podem ser escritos e de que forma eles 
    # podem ser lidos. 

