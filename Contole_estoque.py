from Models.estoque import Estoque
from Models.Produtos_Models import Produtos

estoque = Estoque('estoque.db')


def Add_produto():
    nome = input("Nome: ")
    quantidade = input("Quantidade: ")
    valor = input("Valor: ")

    newProduto = Produtos()
    newProduto.set_prod(nome, quantidade, valor)


    if estoque.Add_Produto(newProduto.get_id(), newProduto.get_nome(), newProduto.get_quantidade(), newProduto.get_preco):
        print("Produto adicionado", newProduto.get_nome())
    else:
        print('Erro ao adicionar produto')
                

def Listar_produtos():
    produtos = estoque.listar_produtos()    
    print(produtos)

def Buscar_produto():
    id = input("ID: ")
    produto = estoque.buscar_produto('produto', id)
    print(produto) 

def Remover_produto():
    id = input("ID: ")
    if estoque.remover_produto('produto', id):
        print("Produto removido")
    else:
        print("Erro ao remover produto")

def Atualizar_produto():
    id = input("ID: ")
    nome = input("Nome: ")
    quantidade = input("Quantidade: ")
    valor = input("Valor: ")

    newProduto = Produtos()
    newProduto.set_prod(nome, quantidade, valor)

    if estoque.atualizar_produto('produto', newProduto.get_prod(), id):
        print("Produto atualizado")
    else:
        print("Erro ao atualizar produto")

def Comprar_produto():
    id = input("ID: ")
    quantidade = input("Quantidade: ")
    if estoque.comprar_produto('produto', id, quantidade):
        print("Produto comprado")
    else:
        print("Erro ao comprar produto")   

def Calcular_valor_total():
    print(estoque.calcular_valor_total())
