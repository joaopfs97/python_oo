class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):  
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        if self.ativo:
            return f'Nome: {self.nome} | Categoria: {self.categoria} | Situação: Ativo'
        else:
            return f'Nome: {self.nome} | Categoria: {self.categoria} | Situação: Inativo'
    
    def lista_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

restaurante_praca = Restaurante('Praça','Gourmet')
restarante_pizza = Restaurante('Pizza Premium','Italiana')
Restaurante.lista_restaurantes()
