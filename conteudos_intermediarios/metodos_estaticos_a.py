# Continuação Métodos estáticos. 

# Quando utilizar métodos e classe e quando 
# quando utilizar métodos estáticos. 


class Produto: 

    pass 

    # Nós utilizamos métodos de classe quando nós queremos utilizar um 
    # método com mais de uma instância, e fazemos isto ao invés de criarmos
    # um método isolado comum. 

    @staticmethod 
    def inteiro():
        pass 

    @classmethod 

    # Agora nós criamos métodos de classe quando queremos trabalhar 
    # com dados estruturados que a nossa classe possua, por exemplo uma 
    # atributo que é uma lista de instâncias, quando temos a chance de 
    # trabalhar com uma grande quantidade de instâncias. 

    def ler_csv(cls):
        pass 


    