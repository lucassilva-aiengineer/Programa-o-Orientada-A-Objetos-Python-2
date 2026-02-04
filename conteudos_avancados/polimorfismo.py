# Polimorfismo 
# Polimorfismo se trata de uma arquitetura, onde se constrói uma classe 
# que pode lidar com situações diferentes ainda possuindo os mesmos formatos. 

class Veiculo:

    def __init__(self, posicao: int = 0):
        self.posicao = posicao 

    def mover_para_frente(self):
        self.posicao += 1
        print("Posição Atual: ", self.posicao)


class Barco(Veiculo):

    pass 

barco = Barco(10)
barco.mover_para_frente()

class Carro(Veiculo):
    pass 

carro = Carro(100)
carro.mover_para_frente()



# Polimorfismo se trata de construir arquiteturas de métodos que servem 
# para diferentes objetos, pois estes objetos se comportam da mesma forma. 

# Exemplo

minha_string = "Nome"
minha_lista = ["A", "B"]

# Lidamos com dois tipos de objetos diferentes, mas ainda fazemos 
# as mesmas coisas. 

print(len(minha_lista))
print(len(minha_string))

# Polimorfismo um método que pode ser utilizado corretamente por diferentes tipos de objetos.
# São situações parecidas para as quais podemos utilizar os mesmo método para resolver.