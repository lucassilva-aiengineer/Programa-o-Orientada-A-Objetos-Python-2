from __future__ import annotations
from typing import List, Union
import csv 

class Produto:

    """Esta é a classe mãe do nosso projeto, a classe produto """

    margem_lucro = 1 + (20 / 100)

    todas_instancias: List[Produto] = []

    def __init__(self, nome: str= "", descricao: Union[str, None]= None, quantidade: int= 0,
    custo: float= 0)-> None:

    # Atributos Privados; métodos públicos.

        self.__nome = nome 
        self.__descricao = descricao 
        self.__quantidade = quantidade 
        self.__custo_unidade = custo 
        self.__valor_unidade = Produto.margem_lucro * self.__custo_unidade
        self.__custo_total = self.__custo_unidade * self.__quantidade
        self.__valor_total = self.__valor_unidade * self.__quantidade 
        self.__lucro_unidade = self.__valor_unidade - self.__custo_unidade 
        self.__lucro_total = self.__lucro_unidade * self.__quantidade 

    # Adicionando objeto ao atributo de classe 

        Produto.todas_instancias.append(self)

    # Ainda não criei o getter 
    # Método de acesso a leitura 

    # Nem o setter método de acesso a escrita. 

    # Criando os getters, métodos de acesso, leitura 

    @property 
    def nome(self)-> str:
        return self.__nome 

    @nome.setter 
    def nome(self, novo_nome)-> None:
        self.__nome = novo_nome 


    def info(self):

        print(f"""====== Relatório ======
        Nome: {self.__nome}.
        -------------------
        Descrição: {self.__descricao if self.__descricao else "Sem descrição."}.
        -------------------
        Quantidade: {self.__quantidade}.
        -------------------
        Custo un: {self.__custo_unidade}.
        -------------------
        Valor un: {self.__valor_unidade}.
        -------------------
        Lucro un: {self.__lucro_unidade}
        -------------------
        Custo Lote: {self.__custo_total}
        --------------------
        Valor total (lucro + custo): {self.__valor_total} 
        ------------------------------------------
        lucro_total: {self.__lucro_total}
        ------------------------------------------""")

    def aplicar_desconto(self)-> float:

        self.__custo_unidade = self.__custo_unidade * self.margem_lucro # Tenta acessar o atributo na instância, caso não encontre 
        # acessa o atributo da classe. 

        return self.__custo_unidade 

    # Abrindo csv 

    @staticmethod 
    def abrir_csv(): 

        """ Esta lê o csv e cria objetos apartir dos dados do csv 
            e como todo objeto criado é adicionado ao atributo de classe
            todos os objetos criados aprtir do csv são alocados no atributo de classe 
            Produto.todas_instancias"""

        with open('projeto_final/dados_empresa.csv', 'r') as f:

            leitor = csv.DictReader(f)
            itens = list(leitor)

            for item in itens: 

                Produto(item["nome"],
                        item["descricao"],
                        int(item["quantidade"]), 
                        float(item["custo"]))



    # Utilizando um método mágico para exibir um atributo. 

    def __repr__(self)-> str:

        return f"{self.__class__.__name__}(\"{self.__nome}\")"

# produto_1 = Produto("Iphone 17", "512 GB | 16 GB ram", 100, 8000) 

# Produto.abrir_csv()
# print(Produto.todas_instancias)