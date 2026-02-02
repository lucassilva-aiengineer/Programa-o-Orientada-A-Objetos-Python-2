from __future__ import annotations
from typing import Union, List 
from typing import Optional

import csv  


class Produto:

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

    @property 
    def descricao(self)-> Optional[str]:
        return self.__descricao 

    @property 
    def quantidade(self)-> int: 
        return self.__quantidade 

    @property 
    def custo_unidade(self)-> float: 
        return self.__custo_unidade 

    @property 
    def valor_unidade(self)-> float:
        return self.__valor_unidade

    # Definindo os setters 
    # as regras de acesso, escrita 

    @nome.setter 
    def nome(self, novo_nome: str)-> None:
        self.__nome = novo_nome 

    @descricao.setter 
    def descricao(self, nova_descricao)-> None:
        self.__descricao = nova_descricao 

    @quantidade.setter 
    def quantidade(self, nova_quantidade: int):
        self.__quantidade = nova_quantidade 

    @custo_unidade.setter 
    def custo(self, novo_custo: float)-> None:
        self.__custo_unidade = novo_custo 

    @valor_unidade.setter 
    def valor_unidade(self, novo_preco: float)-> None: 
        self.__valor_unidade = novo_preco 



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

    # Utilizando um método mágico para exibir um atributo. 

    def __repr__(self)-> str:

        return f"Produto('{self.__nome, self.__quantidade, self.__custo_unidade, self.__lucro_unidade}')"

    # Utilizando um método de classe para acessar o csv e com os dados 
    # dele criar um objeto Produto. 

    # Os métodos de classe são os comportamentos da classe, métodos 
    # que modificam ou criam novos atributos de classe. 

    @classmethod 
    def criar_csv(cls)-> None:

        with open('dados_empresa.csv', 'r') as f: 

            leitor = csv.DictReader(f)
            itens = list(leitor)

        # for item in itens: 
        #     print(item)

        # Melhorando a exibição 

        # for item in itens: 

        #     print("===========================")
        #     print("Nome:", item['nome'], 
        #             "\nDescrição:", item['descricao'],
        #             "\nQuantidade:", item['quantidade'], 
        #             "\nCusto:",item['custo'],
        #             "\nPreço:",item['preco'])

        #     print("===========================")


        # Acessando o csv e transformando os itens do csv em objetos. 

        for item in itens: 

            Produto(item["nome"],
                    item["descricao"],
                    int(item["quantidade"]), 
                    float(item["custo"]))


    # Criando um método estático. 

    @staticmethod 
    def inteiro(numero):

        if isinstance(numero, float): 
            # return inteiro(numero) 
            return False

        elif isinstance(numero, int): 
            return True 

        else: 
            return False 

produto_1 = Produto("Iphone 17", "512 GB | 16 GB ram", 100, 8000)

# print(Produto.todas_instancias)

Produto.criar_csv()


print(Produto.todas_instancias)

print(Produto.inteiro(7.5))