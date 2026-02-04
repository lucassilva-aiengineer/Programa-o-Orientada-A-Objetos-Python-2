# Abstração, abstração é um princípio em python onde temos 
# métodos que funcionam são visíveis apenas no interior da classe 
# e são utilizados por métodos públicos visíeis a usuário. 

from encapsulamento import Produto 

produto_a = Produto("Produto", 100, 1000, 1200)

# Nós temos um método público que utiliza métodos privados não visíveis aos usuários. 

produto_a.enviar_email()