# Introdução 


# item_1 = 'phone'
# item_1_quantidade = 10 

class Item: 

    pass 

item1 = Item()

# random_str = str("4")


# Associando atributos a um objeto

item1.nome = "Telefone"
item1.preco = 100  
item1.quantidade = 5 

print(type(item1))
print(item1.nome)
print(item1.preco)
print(item1.quantidade)

string_aleatoria = "string_texto"

# Os tipos primitivos de dados possuem métodos. 
print(string_aleatoria.upper())


class Produto:

    def preco_total(self, quantidade: int, preco: float)-> float:
        return quantidade * preco


produto_a = Produto()

produto_a.nome = "Mesa"
produto_a.quantidade = 10
produto_a.preco = 5 

preco_total = produto_a.preco_total(produto_a.quantidade, produto_a.preco)

print(preco_total)