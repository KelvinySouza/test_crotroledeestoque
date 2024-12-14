from Models.Database import Banco_de_produtos

class Produtos(Banco_de_produtos):
    def __init__(self):
        super().__init__('estoque.db')
        self.__id = None
        self.__name = ''
        self.__quantidade = ''
        self.__preco = ''
        
    def set_prod(self, nome, quant, preco):
        self.__name = nome
        self.__quantidade = quant
        self.__preco = preco

    def get_nome(self):
        return self.__name
    
    def get_quantidade(self):
        return self.__quantidade
    
    def get_preco(self):
        return self.__preco
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
        
    def set_name(self, name):
        self.__name = name
        
    def set_quantidade(self, quant):
        self.__quantidade = quant
        
    def set_preco(self, preco):
        self.__preco = preco
        
    def __str__(self):
        return f'ID: {self.__id}\nNome: {self.__name}\nQuantidade: {self.__quantidade}\nPreco: {self.__preco}'
        
  