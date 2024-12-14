from Models.estoque import Estoque
from Models.Produtos_Models import Produtos
from Models.Database import Banco_de_produtos
from Models.Produtos_Models import Produtos

def main():

    while True:
        print('''\033[32m
        ################################################################
        # ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗   ██╗███████╗ #
        # ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║   ██║██╔════╝ #
        # █████╗  ███████╗   ██║   ██║   ██║██║   ██║██║   ██║█████╗   #
        # ██╔══╝  ╚════██║   ██║   ██║   ██║██║▄▄ ██║██║   ██║██╔══╝   #
        # ███████╗███████║   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗ #
        # ╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝ #
        ################################################################ \033[0m''')
        print("Menu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar produto")
        print("4. Listar produtos")
        print("5. Buscar produto")
        print("6. Comprar")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        
        estoque = Estoque('estoque.db')
        banco = Banco_de_produtos('estoque.db')


        if escolha == '4' or escolha == '5' or escolha == '6' or escolha == '7' or escolha == '8' or escolha == '9' or escolha == '10':
            estoque = Banco_de_produtos('estoque.db')

        if escolha == '0':
            break

        match escolha:
            case '1':
                nome = input("Nome: ")
                quantidade = input("Quantidade: ")
                valor = input("Valor: ")
            

                newProduto = Produtos()
                newProduto.set_prod(nome, quantidade, valor)
                

                if estoque.Add_Produto(newProduto.get_id(), newProduto.get_nome(), newProduto.get_quantidade(), newProduto.get_preco):
                    print("Produto adicionado", newProduto.get_nome())
                else:
                    print('Erro ao adicionar produto')

                input("Pressione Enter para continuar...")
                

            case '2':
          
                id = input("Id: ")
                estoque.remover_produto('produto', id)  
                input("Pressione Enter para continuar...")

            case '3':
                id = input("Id: ")
                nome = input("Nome: ")
                quantidade = input("Quantidade: ")
                valor = input("Valor: ")
                estoque.atualizar_produto('produto', id, nome, quantidade, valor)
                input("Pressione Enter para continuar...")


            case '4':
                estoque.listar_produtos()
                get__all = estoque.get_all('produto')
                for i in get__all:
                    print(i)

                input("Pressione Enter para continuar...")




            case '5':
                id = input("Id: ")
                estoque.buscar_produto('produto', id)
                input("Pressione Enter para continuar...")

            case '6':
                id = input("Id: ")
                estoque.comprar_produto('produto', id)
                input("Pressione Enter para continuar...")
            
                
            case '0':
                exit()
            
            case _:
                print("Opção inválida")

if __name__ == '__main__':
    main()