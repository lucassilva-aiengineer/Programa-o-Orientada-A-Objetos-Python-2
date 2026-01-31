from typing import Union

class Produto:

    margem_lucro = 1 + (20 / 100)

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

    # Ainda não criei o getter 
    # Método de acesso a leitura 

    # Nem o setter método de acesso a escrita. 

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

produto_1 = Produto("Iphone 17", "512 GB | 16 GB ram", 100, 8000)

# produto_1.info() 

print(produto_1.__dict__) # Acessando todos os atributos a nível de instância. 
print(Produto.__dict__)   # Acessando todos os atributos a nível de classe.


# Caso desejemos alterar uma taxa nível de classe, basta criarmos 
# um atributo de taxa relacionado apenas a instância

produto_2 = Produto("Galaxy S22", "Armazenamento 1T | 32GB ram", 100, 10000)

# produto_2.margem_lucro = 80 / 100 

print(produto_2.aplicar_desconto())