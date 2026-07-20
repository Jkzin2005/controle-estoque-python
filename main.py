from estoque import cadastrar,listar,remover_produto,atualizar_qtd_produto,salvar_arquivo,carregar_arquivo, gerar_id,atualizar_preco_produto, buscar_produto

try:
    produtos = carregar_arquivo()
except:
    produtos = []
def menu():
    while True:
        print("------CONTROLE DE ESTOQUE------")
        print("1 - Cadastrar produto")
        print("2 - Listar produto")
        print("3 - Atualizar quantidade")
        print("4 - Atualizar preço")
        print("5 - Buscar produto")
        print("6 - Remover produto")
        print("7 - Sair")

        opcao = input("ESCOLHA UMA OPCAO: ")
                
        if opcao == "1":
            cadastrar(produtos)
            salvar_arquivo(produtos)
            
        elif opcao == "2":
            listar(produtos)
            
        elif opcao == "3":
            print("Quantidade atualizada")
            atualizar_qtd_produto(produtos)
            salvar_arquivo(produtos)

        elif opcao == "4":
            print("Preço atualizado")
            atualizar_preco_produto(produtos)
            salvar_arquivo(produtos)
        
        elif opcao == "5":
            print("Buscando produto")
            buscar_produto(produtos)
            
        elif opcao == "6":
            remover_produto(produtos)  
            salvar_arquivo(produtos)
        
        elif opcao == "7":
            print("SAINDO DO MENU")  
            salvar_arquivo(produtos)
                
        else:
            print("OPÇAO INVALIDA")

menu()