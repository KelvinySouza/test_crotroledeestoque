from Models.Produtos_Models import Produtos

class Estoque(Produtos):
    def __init__(self, bd):
        super().__init__(bd)
        self.__table = {
            'table': 'produto',
            'colums': {
                'id': 'Text',
                'name': 'Text',
                'quantidade': 'int',
                'value': 'real'
            }
        }
        self.create_table(self.__table['table'], self.__table['colums'])

    def Add_Produto(self, id, nome, quantidade, valor):
        prod = {
            'table': 'produto',
            'values': {
                'id':id,
                'name': nome,
                'quantidade':quantidade,
                'value': valor
            }
        }

        return self.insert_values(prod['table'], prod['values'])
    
    def listar_produtos(self):
        return self.get_all(self.__table['table']) 

    def atualizar_produto(self, table, values, condition):
        return self.update_values(table, values, condition)

    def remover_produto(self, table, condition):
        return self.delete_values(table, condition)

    def buscar_produto(self, table, id):
        return self.get_value_id(table, id)

    def calcular_valor_total(self):
        return self.get_value(self.__table['table'], {'where': 'quantidade > 0'})
    