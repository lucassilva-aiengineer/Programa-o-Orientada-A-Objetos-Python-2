

class Item:

    def __init__(self, nome: str, preco: float= 200, quantidade: int= 0)-> None:

        assert preco >= 0, "O preco do produto deve ser maior ou igual a zero"
        assert quantidade >= 0, f"A quantidade deve ser maior ou igual a 0, quantidade atual: {quantidade}" # Caso nçao seja cumprida teremos um AssertioError. 

        self.nome = nome 
        self.preco = preco 
        self.quantidade = quantidade 

        print("Objeto criado...")
        print("Id", id(self))


    def preco_total(self)-> float:

        resultado = self.preco * self.quantidade

        print(f"preco total: {resultado}")
        return resultado 

objeto_1 = Item("telefone", 100, 10)
objeto_2 = Item("laptop", 500, 20)

# Criando atributos específicos para certos 
# objetos 

# objeto_2.numpad = True 

# print(objeto_2.numpad)

print(objeto_1.preco_total())

try:

    objeto_3 = Item("SmartTv", 200, -5)

except AssertionError as message:
    print(message)

    print("Tentando novamente...")

    quantidade = int(input("Indique uma quantidade válida: "))
    objeto_3 = Item("SmartTv", 300, quantidade)

else:
    print("Código executado sem erros...")

finally: 
    print("Código executado.")