# Encapsulamento restrição de acesso diréto a atributos. 


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

    # Definimos uma lógica bem simples onde o acessoa leitura é livre, como se o atributo 
    # fosse público, e na verdade não. 


    @property 
    def nome(self)-> str:
        return self.__nome 

    @property 
    def quantidade(self)-> int:
        return self.__quantidade 

    @property 
    def custo(self)-> float: 
        return self.__custo 

    @property 
    def preco(self)-> float:
        return self.__preco 

    # Setters 

    # Definindo o acesso a lógica que permite a escrita dos atributos, 
    # no caso temos uma regra simples que permite uma alteração como se 
    # o atributo fosse pública, mas não é o caso. 

    @nome.setter 
    def nome(self, novo_nome: str)-> None:

        if not novo_nome.startswith("A"):
            self.__nome = novo_nome
        else:
            print("O novo nome não pode começar com a letra A!")
            time.sleep(2)



    @quantidade.setter 
    def quantidade(self, nova_quantidade: int)-> None:
        self.__quantidade = nova_quantidede 

    @custo.setter 
    def custo(self, novo_custo: float)-> None:
        self.__custo = novo_custo 

    @preco.setter 
    def preco(self, novo_preco)-> None:
        self.__preco = novo_preco 


    # Método mágico que retorna uma string quando imprimimos os objetos desta classe, ao invés. 

    def __repr__(self):

        return f"{self.__nome}"



produto_a = Produto("Iphone 17", 100, 500, 800)
print(produto_a)

print(produto_a.nome)
produto_a.nome = "Aphone 18" # Não aleteramos o atributo original, apenas criamos um novo. 

print(produto_a.nome)