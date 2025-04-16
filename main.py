from produto import Produto
from venda import Venda

def menu():
    while True:
        print("\n====== MENU LOJA ======")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Atualizar estoque")
        print("4. Realizar venda")
        print("5. Deletar produto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            descricao = input("Descrição: ")
            qtd = int(input("Quantidade em estoque: "))
            preco = float(input("Preço: "))
            p = Produto(nome, descricao, qtd, preco)
            p.salvar()
            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            produtos = Produto.listar_todos()
            if not produtos:
                print("📭 Nenhum produto cadastrado.")
            else:
                for p in produtos:
                    print(p)

        elif opcao == "3":
            id_prod = int(input("ID do produto a atualizar: "))
            nova_qtd = int(input("Nova quantidade de estoque: "))
            produtos = Produto.listar_todos()
            produto = next((p for p in produtos if p.id == id_prod), None)
            if produto:
                produto.qtd_estoque = nova_qtd
                produto.salvar()
                print("Estoque atualizado.")
            else:
                print("Produto não encontrado.")

        elif opcao == "4":
            id_prod = int(input("ID do produto vendido: "))
            qtd_vendida = int(input("Quantidade vendida: "))
            try:
                venda = Venda(id_do_produto=id_prod, qtd_vendida=qtd_vendida)
                venda.salvar()
                print("Venda registrada.")
            except ValueError as e:
                print(f"Erro ao realizar venda: {e}")

        elif opcao == "5":
            id_prod = int(input("ID do produto a deletar: "))
            produtos = Produto.listar_todos()
            produto = next((p for p in produtos if p.id == id_prod), None)
            if produto:
                produto.deletar()
                print("Produto e vendas associadas deletados com sucesso.")
            else:
                print("Produto não encontrado.")


        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
