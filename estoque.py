import json


def salvar_arquivo(produtos):
    with open("dados.json", "w") as arquivo:
        json.dump(produtos, arquivo)
    


def carregar_arquivo():
    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)
        return dados
    
try:
    produtos = carregar_arquivo()
except FileNotFoundError:
    produtos = []
        
def gerar_id(produtos):
    if not produtos:
        return 1
    maior_id = max(p["id"] for p in produtos)
    return maior_id + 1

def cadastrar(produtos):
        id_produto = gerar_id(produtos)
        nome    = input("Digite o nome do produto: ")
        while True:
            try:
                qtd = input("Digite a quantiade de produtos: ")
                valor = input("Digite o preço do produto: ")
                qtd = int(qtd)
                valor = float(valor)
                break
            except ValueError: 
                print("DIGITE APENAS NUMEROS!!")
                
        produto_existe = False
        
        novoProduto = {
            'id': id_produto ,
            'nome': nome   ,
            'quantidade': qtd,
            'preco': valor}   
        print("Cadastrando produto")
        
        for p in produtos:
            if p["nome"] == nome:
                print("ESSE PRODUTO JA EXISTE!!!!")
                produto_existe = True
        if not produto_existe: 
            produtos.append(novoProduto)

         
def listar(produtos):
    for p in produtos:
        print("ID: ", p ["id"])
        print("PRODUTO: ", p["nome"])
        print("QUANTIDADE: ", p["quantidade"])
        print("PREÇO: R$", p["preco"])
        
def remover_produto(produtos):
    user_remove = input("DIGITE O ID DO PRODUTO QUE DESEJA REMOVER: ")
    try:
        user_remove = int(user_remove)
    except ValueError:
        print("ID INVALIDO")
        return
    encontrou = False
    for p in produtos:
        if user_remove == p["id"]:
            user_confirma = input("TEM CERTEZA QUE DESEJA REMOVER? S/N: ").lower()
            if user_confirma == "s":
                produto_remover = p
                encontrou = True
                produtos.remove(produto_remover)
                print("Produto: ",p["nome"],"ID: ",p["id"], "removido")
                break
            elif user_confirma == "n":
                encontrou = True
                print("VOLTANDO AO MENU")
                break
            else:
                print("OPCAO INVALIDA")
                return
    if not encontrou:
        print("PRODUTO NAO ENCONTRADO")
    
        
def atualizar_qtd_produto(produtos):
    user_atualiza_id = input("Digite o ID do que produto deseja atualizar? ")
    user_quantidade = input("DIGITE A quantidade: ")
    try:
        user_atualiza_id = int(user_atualiza_id)
        user_quantidade = int(user_quantidade)
    except ValueError:
        print("ID OU QUANTIDADE INVALIDADE")
        return
    encontrou = False
    
    for p in produtos:
        
        if p["id"] == user_atualiza_id:
            p["quantidade"] = user_quantidade
            print("QUANTIDADE ATUALIZADA\nProduto: ",p["nome"],"ID: ",p["id"])
            encontrou = True
            break
            
    if encontrou == False:
        print("PRODUTO NAO ENCONTRADO")
        
def atualizar_preco_produto(produtos):
    user_atualiza_preco_id = input("Digite o ID do que produto deseja atualizar? ")
    user_atualiza_preco = input("Digite o novo preço ")
    
    try:
        user_atualiza_preco_id = int(user_atualiza_preco_id)
        user_atualiza_preco = float(user_atualiza_preco)
    except ValueError:
        print("ID OU PREÇO INVALIDO")
        return
    encontrou = False
    
    for p in produtos:
        if p["id"] == user_atualiza_preco_id:
            p["preco"] = user_atualiza_preco
            print("PREÇO ATUALIZADO\nProduto: ",p["nome"],"ID: ",p["id"])
            encontrou = True
            break
            
    if not encontrou:
        print("Produto nao encontrado")
    
def buscar_produto(produtos):
    user_busca_id = input("Digite o ID que seja buscar ") 
    try:
        user_busca_id = int(user_busca_id)
    except ValueError:
        print("ID INVALIDO") 
        return
    encontrou = False
    
    for p in produtos:
        if p["id"] == user_busca_id:
            print("ID: ", p ["id"])
            print("PRODUTO: ", p["nome"])
            print("QUANTIDADE: ", p["quantidade"])
            print("PREÇO: ", p["preco"])   
            encontrou = True
            break
            
    if not encontrou:
        print("ID nao encontrado")    