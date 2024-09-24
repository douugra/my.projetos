import os

def gotoxy(x,y): 
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def printRed(s):
    print(f"\033[31m{s}\033[m")

def printGreen(s):
    print(f"\033[32m{s}\033[m")

def printBlue(s):
    print(f"\033[34m{s}\033[m")

def printLI(s):
    print(f"\033[1;34m{s}\033[m")

def printCyt(s):
    print(f"\033[0;36m{s}\033[m")

def printYELLOW(s):
    print(f"\033[1;33m{s}\033[m")

def autenticar():
    os.system("cls")
    senha_correta = "Tripulação"
    tentativas = 3

    while tentativas > 0:
        senha = input("\033[1;33mDigite a senha de acesso: ")
        if senha == senha_correta:
            print("Autenticado com sucesso!")
            return True
        else:
            tentativas -= 1
            printRed(f"Senha incorreta. Tentativas restantes: {tentativas}")
    
    printRed("Acesso negado.")
    return False

            
def cadastrar_produto():
    try:
        printGreen("▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜")
        printGreen("▌             \033[34mCadasTrar Poduto\033[m \033[32m               ▐")
        printGreen("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")
        printGreen("▌                                             ▐")
        codigo = int(input("\033[32m▌\033[34m Digite o código do produto: "))
        nome = input("\033[32m▌\033[34m Digite o nome do produto: ")
        descricao = input("\033[32m▌\033[34m Digite a descrição do produto: ")
        preco_compra = float(input("\033[32m▌\033[34m Digite o preço de compra do produto: "))
        preco_venda = float(input("\033[32m▌\033[34m Digite o preço de venda do produto: "))
        estoque = 0  # Inicialmente o estoque é zero
        printGreen("▌                                             ▐")
        printGreen("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")
        with open("produtos.txt", "a", encoding="utf8") as arquivo:
            arquivo.write(f"{codigo};{nome};{descricao};{preco_compra};{preco_venda};{estoque}\n")
        
        printGreen("Produto cadastrado com sucesso!")
    except:
        printRed(f"Erro ao cadastrar produto: ")
    input("\033[32mPrecione Enter Para Sair")

def remover_produto():
    try:
        codigo = input("Digite o código do produto a ser removido: ")
        
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            produto_encontrado = False
            for produto in produtos:
                if not produto.startswith(codigo + ";"):
                    arquivo.write(produto)
                else:
                    produto_encontrado = True
        
        if produto_encontrado:
            remover_registros_associados(codigo)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao remover produto: {e}")
    

def remover_registros_associados(codigo_produto):
    try:
        with open("compras.txt", "r", encoding="utf8") as arquivo:
            compras = arquivo.readlines()
        
        with open("compras.txt", "w", encoding="utf8") as arquivo:
            for compra in compras:
                if not compra.split(";")[2] == codigo_produto:
                    arquivo.write(compra)
        
        with open("vendas.txt", "r", encoding="utf8") as arquivo:
            vendas = arquivo.readlines()
        
        with open("vendas.txt", "w", encoding="utf8") as arquivo:
            for venda in vendas:
                if not venda.split(";")[2] == codigo_produto:
                    arquivo.write(venda)
        
    except:
        printRed(f"Erro ao remover registros associados: ")
    input("\033[32mPrecione Enter Para Sair")
    
def atualizar_produto():
    try:
        codigo = input("Digite o código do produto a ser atualizado: ")
        
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        produto_encontrado = False
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            for produto in produtos:
                if produto.startswith(codigo + ";"):
                    nome = input("Digite o novo nome do produto: ")
                    descricao = input("Digite a nova descrição do produto: ")
                    preco_compra = float(input("Digite o novo preço de compra: "))
                    preco_venda = float(input("Digite o novo preço de venda: "))
                    estoque = int(input("Digite o estoque atual do produto: "))
                    arquivo.write(f"{codigo};{nome};{descricao};{preco_compra};{preco_venda};{estoque}\n")
                    produto_encontrado = True
                else:
                    arquivo.write(produto)
        
        if produto_encontrado:
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")
    input("\033[32mPrecione Enter Para Sair")


def comprar_produto():
    try:
        codigo_produto = input("Digite o código do produto que deseja comprar: ")
        quantidade = int(input("Digite a quantidade comprada: "))
        codigo_compra = input("Digite o código da compra: ")
        data_compra = input("Digite a data da compra (dd/mm/aaaa): ")
        
        produto_encontrado = False
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            for produto in produtos:
                dados = produto.strip().split(";")
                if dados[0] == codigo_produto:
                    estoque_atual = int(dados[5])
                    novo_estoque = estoque_atual + quantidade
                    arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    produto_encontrado = True
                else:
                    arquivo.write(produto)
        
        if produto_encontrado:
            with open("compras.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(f"{codigo_compra};{data_compra};{codigo_produto};{quantidade}\n")
            print("Compra registrada com sucesso!")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao registrar compra: {e}")
    input("\033[32mPrecione Enter Para Sair")


def registrar_venda():
    try:
        codigo_produto = input("Digite o código do produto que deseja vender: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        codigo_venda = input("Digite o código da venda: ")
        data_venda = input("Digite a data da venda (dd/mm/aaaa): ")
        
        produto_encontrado = False
        estoque_suficiente = False
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            for produto in produtos:
                dados = produto.strip().split(";")
                if dados[0] == codigo_produto:
                    estoque_atual = int(dados[5])
                    if quantidade <= estoque_atual:
                        estoque_suficiente = True
                        novo_estoque = estoque_atual - quantidade
                        arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    else:
                        print("Não temos essa quantidade disponível no momento.")
                        arquivo.write(produto)  # Reescreve o produto sem alterar o estoque
                        return
                    produto_encontrado = True
                else:
                    arquivo.write(produto)
        
        if produto_encontrado and estoque_suficiente:
            with open("vendas.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(f"{codigo_venda};{data_venda};{codigo_produto};{quantidade}\n")
            print("Venda registrada com sucesso!")
        elif not produto_encontrado:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao registrar venda: {e}")
    input("\033[32mPrecione Enter Para Sair")
        


def listar_produtos():
    try:
        produtos_encontrados = False
        produtos_existentes = False
        printBlue(f"\n{'Código':<10}{'Nome':<30}{'Total Comprado':<15}{'Total Vendido':<15}")
        
        # Verificar se o arquivo de produtos existe e está acessível
        try:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            if not produtos:
                printRed("Não tem movimentações.")
                return
            
            for produto in produtos:
                dados = produto.strip().split(";")
                codigo_produto = dados[0]
                nome_produto = dados[1]
                
                quantidade_comprada_total = 0
                quantidade_vendida_total = 0
                
                # Ler o arquivo de compras
                try:
                    with open("compras.txt", "r", encoding="utf8") as arquivo:
                        compras = arquivo.readlines()
                    
                    for compra in compras:
                        dados_compra = compra.strip().split(";")
                        if dados_compra[2] == codigo_produto:
                            quantidade_comprada_total += int(dados_compra[3])
                except FileNotFoundError:
                    pass
                
                # Ler o arquivo de vendas
                try:
                    with open("vendas.txt", "r", encoding="utf8") as arquivo:
                        vendas = arquivo.readlines()
                    
                    for venda in vendas:
                        dados_venda = venda.strip().split(";")
                        if dados_venda[2] == codigo_produto:
                            quantidade_vendida_total += int(dados_venda[3])
                except FileNotFoundError:
                    pass
                
                
                if quantidade_comprada_total > 0 or quantidade_vendida_total > 0:
                    produtos_encontrados = True
                    produtos_existentes = True
                    printBlue(f"{codigo_produto:<10}{nome_produto:<30}{quantidade_comprada_total:<15}{quantidade_vendida_total:<15}")
        
        except FileNotFoundError:
            printRed("Não tem movimentações.")
            return
        
        if not produtos_existentes:
            printRed("Não tem movimentações.")
    except Exception as e:
        printRed(f"Erro ao listar produtos: {e}")
    input("\033[32mPrecione Enter Para Sair")
    

def cancelar_venda():
    try:
        codigo_venda = input("Digite o código da venda a ser cancelada: ")
        produto_encontrado = False
        quantidade_cancelada = 0
        codigo_produto = None
        
        with open("vendas.txt", "r", encoding="utf8") as arquivo:
            vendas = arquivo.readlines()
        
        with open("vendas.txt", "w", encoding="utf8") as arquivo:
            for venda in vendas:
                dados = venda.strip().split(";")
                if dados[0] == codigo_venda:
                    produto_encontrado = True
                    quantidade_cancelada = int(dados[3])
                    codigo_produto = dados[2]
                else:
                    arquivo.write(venda)
        
        if produto_encontrado:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            with open("produtos.txt", "w", encoding="utf8") as arquivo:
                for produto in produtos:
                    dados = produto.strip().split(";")
                    if dados[0] == codigo_produto:
                        estoque_atual = int(dados[5])
                        novo_estoque = estoque_atual + quantidade_cancelada
                        arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    else:
                        arquivo.write(produto)
            
            print("Venda cancelada com sucesso!")
        else:
            print("Venda não encontrada.")
    except Exception as e:
        print(f"Erro ao cancelar venda: {e}")
    input("\033[32mPrecione Enter Para Sair")
    
def detalhes_produto():
    try:
        codigo_produto = input("Digite o código do produto: ")
        
        produto_info = None
        quantidade_comprada_total = 0
        quantidade_vendida_total = 0
        valor_total_compra = 0
        valor_total_venda = 0
        
        try:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            for produto in produtos:
                dados = produto.strip().split(";")
                if dados[0] == codigo_produto:
                    produto_info = {
                        'nome': dados[1],
                        'descricao': dados[2],
                        'preco_compra': float(dados[3]),
                        'preco_venda': float(dados[4]),
                        'estoque': int(dados[5])
                    }
                    break
            
            if produto_info:
                print(f"\nDetalhes do Produto")
                print(f"Nome: {produto_info['nome']}")
                print(f"Descrição: {produto_info['descricao']}")
                print(f"Preço de Compra: {produto_info['preco_compra']:.2f}")
                print(f"Preço de Venda: {produto_info['preco_venda']:.2f}")
                print(f"Estoque Atual: {produto_info['estoque']}")
                
                movimentos_encontrados = False
                print(f"\n{'Código Compra':<15}{'Data':<12}{'Quantidade Comprada':<20}")
                
                try:
                    with open("compras.txt", "r", encoding="utf8") as arquivo:
                        compras = arquivo.readlines()
                    
                    for compra in compras:
                        dados_compra = compra.strip().split(";")
                        if dados_compra[2] == codigo_produto:
                            movimentos_encontrados = True
                            quantidade_comprada_total += int(dados_compra[3])
                            valor_total_compra += produto_info['preco_compra'] * int(dados_compra[3])
                            print(f"{dados_compra[0]:<15}{dados_compra[1]:<12}{dados_compra[3]:<20}")
                except FileNotFoundError:
                    pass
                
                print(f"\n{'Código Venda':<15}{'Data':<12}{'Quantidade Vendida':<20}")
                
                try:
                    with open("vendas.txt", "r", encoding="utf8") as arquivo:
                        vendas = arquivo.readlines()
                    
                    for venda in vendas:
                        dados_venda = venda.strip().split(";")
                        if dados_venda[2] == codigo_produto:
                            movimentos_encontrados = True
                            quantidade_vendida_total += int(dados_venda[3])
                            valor_total_venda += produto_info['preco_venda'] * int(dados_venda[3])
                            print(f"{dados_venda[0]:<15}{dados_venda[1]:<12}{dados_venda[3]:<20}")
                except FileNotFoundError:
                    pass
                
                if not movimentos_encontrados:
                    print("Não tem movimentações.")
                
                lucro_total = valor_total_venda - valor_total_compra
                
                print(f"\nQuantidade Total Comprada: {quantidade_comprada_total}")
                print(f"Quantidade Total Vendida: {quantidade_vendida_total}")
                print(f"Valor Total Investido: {valor_total_compra:.2f}")
                print(f"Valor Total Arrecadado: {valor_total_venda:.2f}")
                print(f"Lucro Obtido: {lucro_total:.2f}")
            else:
                print("Produto não encontrado.")
        except FileNotFoundError:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao mostrar detalhes do produto: {e}")
    input("\033[32mPrecione Enter para Sair")

def listar_todas_vendas():
    try:
        # Abre o arquivo de vendas e lê todas as linhas
        with open("vendas.txt", "r", encoding="utf8") as arquivo:
            vendas = arquivo.readlines()

        # Verifica se o arquivo de vendas está vazio
        if not vendas:
            print("Nenhuma venda registrada.")
            input("\033[32mPrecione Enter Para Sair")
            return

        # Exibe um cabeçalho para as vendas
        printBlue(f"\n{'Código Venda':<15}{'Data':<12}{'Código Produto':<15}{'Quantidade Vendida':<20}")

        # Itera sobre cada linha do arquivo e exibe as informações de venda
        for venda in vendas:
            dados_venda = venda.strip().split(";")
            print(f"{dados_venda[0]:<15}{dados_venda[1]:<12}{dados_venda[2]:<15}{dados_venda[3]:<20}")

    except FileNotFoundError:
        printRed("Arquivo de vendas não encontrado.")

    except Exception as e:
        printRed(f"Erro ao listar vendas: {e}")
    input("\033[32mPrecione Enter Para Sair")

def saldo_financeiro():
    try:
        total_investido = 0
        total_arrecadado = 0
        
        produtos_existentes = False
        
        try:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            for produto in produtos:
                dados = produto.strip().split(";")
                codigo_produto = dados[0]
                preco_compra = float(dados[3])
                preco_venda = float(dados[4])
                
                quantidade_comprada_total = 0
                try:
                    with open("compras.txt", "r", encoding="utf8") as arquivo:
                        compras = arquivo.readlines()
                    
                    for compra in compras:
                        dados_compra = compra.strip().split(";")
                        if dados_compra[2] == codigo_produto:
                            quantidade_comprada_total += int(dados_compra[3])
                except FileNotFoundError:
                    pass
                
                total_investido += preco_compra * quantidade_comprada_total
                
                quantidade_vendida_total = 0
                try:
                    with open("vendas.txt", "r", encoding="utf8") as arquivo:
                        vendas = arquivo.readlines()
                    
                    for venda in vendas:
                        dados_venda = venda.strip().split(";")
                        if dados_venda[2] == codigo_produto:
                            quantidade_vendida_total += int(dados_venda[3])
                except FileNotFoundError:
                    pass
                
                total_arrecadado += preco_venda * quantidade_vendida_total
            
            lucro_total = total_arrecadado - total_investido
            
            if total_investido > 0 or total_arrecadado > 0:
                print(f"\nTotal Investido: {total_investido:.2f}")
                print(f"Total Arrecadado: {total_arrecadado:.2f}")
                
                if lucro_total > 0:
                    print(f"Lucro Acumulado: {lucro_total:.2f}")
                else:
                    print(f"Lucro Acumulado: 0.00 - Não há lucro positivo.")
            else:
                print("Não tem movimentações.")
        except FileNotFoundError:
            print("Não tem movimentações.")
    except Exception as e:
        print(f"Erro ao calcular saldo financeiro: {e}")
    input("\033[32mPrecione Enter para Sair")

def cancelar_compra():
    try:
        codigo_compra = input("Digite o código da compra a ser cancelada: ")
        produto_encontrado = False
        quantidade_cancelada = 0
        codigo_produto = None
        
        with open("compras.txt", "r", encoding="utf8") as arquivo:
            compras = arquivo.readlines()
        
        with open("compras.txt", "w", encoding="utf8") as arquivo:
            for compra in compras:
                dados = compra.strip().split(";")
                if dados[0] == codigo_compra:
                    produto_encontrado = True
                    quantidade_cancelada = int(dados[3])
                    codigo_produto = dados[2]
                else:
                    arquivo.write(compra)
        
        if produto_encontrado:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            with open("produtos.txt", "w", encoding="utf8") as arquivo:
                for produto in produtos:
                    dados = produto.strip().split(";")
                    if dados[0] == codigo_produto:
                        estoque_atual = int(dados[5])
                        novo_estoque = estoque_atual - quantidade_cancelada
                        arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    else:
                        arquivo.write(produto)
            
            print("Compra cancelada com sucesso!")
        else:
            print("Compra não encontrada.")
    except Exception as e:
        print(f"Erro ao cancelar compra: {e}")
    input("\033[32mPrecione Enter para Sair")

def menu_principal():
    while True:
        os.system("cls")
        printYELLOW("▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜")
        printYELLOW("▌                                                                                                      ▐")
        printYELLOW("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")


        gotoxy(34,2)
        printCyt(" ▀▀▀▀▀ Bem-vindo ao Menu Principal! ▀▀▀▀▀  ")

        gotoxy(4,5)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(4,6)
        printYELLOW(f"│                          │")
        gotoxy(4,7)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(38,5)
        printYELLOW(f"┌────────────────────────────┐")
        gotoxy(38,6)
        printYELLOW(f"│                            │")
        gotoxy(38,7)
        printYELLOW(f"└────────────────────────────┘")

        gotoxy(74,5)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(74,6)
        printYELLOW(f"│                          │")
        gotoxy(74,7)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(4,10)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(4,11)
        printYELLOW(f"│                          │")
        gotoxy(4,12)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(38,10)
        printYELLOW(f"┌────────────────────────────┐")
        gotoxy(38,11)
        print(f"│                            │")
        gotoxy(38,12)
        printYELLOW(f"└────────────────────────────┘")

        gotoxy(74,10)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(74,11)
        print(f"│                          │")
        gotoxy(74,12)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(4,10)
        printLI(f"┌──────────────────────────┐")
        gotoxy(4,11)
        printBlue(f"│                          │")
        gotoxy(4,12)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(38,10)
        printYELLOW(f"┌────────────────────────────┐")
        gotoxy(38,11)
        printYELLOW(f"│                            │")
        gotoxy(38,12)
        printYELLOW(f"└────────────────────────────┘")

        gotoxy(74,10)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(74,11)
        printYELLOW(f"│                          │")
        gotoxy(74,12)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(4,10)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(4,11)
        printYELLOW(f"│                          │")
        gotoxy(4,12)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(38,10)
        printYELLOW(f"┌────────────────────────────┐")
        gotoxy(38,11)
        printYELLOW(f"│                            │")
        gotoxy(38,12)
        printYELLOW(f"└────────────────────────────┘")

        gotoxy(74,10)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(74,11)
        printYELLOW(f"│                          │")
        gotoxy(74,12)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(4,16)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(4,17)
        printYELLOW(f"│                          │")
        gotoxy(4,18)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(38,16)
        printYELLOW(f"┌────────────────────────────┐")
        gotoxy(38,17)
        printYELLOW(f"│                            │")
        gotoxy(38,18)
        printYELLOW(f"└────────────────────────────┘")

        gotoxy(74,16)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(74,17)
        printYELLOW(f"│                          │")
        gotoxy(74,18)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(4,20)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(4,21)
        printYELLOW(f"│                          │")
        gotoxy(4,22)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(74,20)
        printYELLOW(f"┌──────────────────────────┐")
        gotoxy(74,21)
        printYELLOW(f"│                          │")
        gotoxy(74,22)
        printYELLOW(f"└──────────────────────────┘")

        gotoxy(38,20)
        printYELLOW(f"┌────────────────────────────┐")
        gotoxy(38,21)
        printYELLOW(f"│                            │")
        gotoxy(38,22)
        printYELLOW(f"└────────────────────────────┘")


        gotoxy(6,6); printBlue("1. Cadastrar Produto")
        gotoxy(41,6); printBlue("2. Listar Produtos")
        gotoxy(77,6); printBlue("3. Registrar Compra")
        gotoxy(6,11); printBlue("4. Registrar Venda")
        gotoxy(41,11); printBlue("5. Detalhes do Produto")
        gotoxy(77,11); printBlue("6. Listar Todas as Vendas")
        gotoxy(6,17); printBlue("7. Relatório Financeiro")
        gotoxy(41,17); printBlue("8. Atualizar Produto")
        gotoxy(77,17); printBlue("9. Cancelar Venda")
        gotoxy(42,21); printBlue("10. Cancelar Produtos")
        gotoxy(6,21); printBlue("11. Remover Produto")
        gotoxy(76,21); printRed("12. Sair")


        
        gotoxy(4,24); opcao = input("\033[32mEscolha uma opção: ")

        if opcao == '1':
            os.system("cls")
            cadastrar_produto()
        elif opcao == '2':
            os.system("cls")
            listar_produtos()
        elif opcao == '3':
            os.system("cls")
            comprar_produto()
        elif opcao == '4':
            os.system("cls")
            registrar_venda()
        elif opcao == '5':
            os.system("cls")
            detalhes_produto()
        elif opcao == '6':
            os.system("cls")
            listar_todas_vendas()
        elif opcao == '7':
            os.system("cls")
            saldo_financeiro()
        elif opcao == '8':
            os.system("cls")
            atualizar_produto()
        elif opcao == '9':
            os.system("cls")
            cancelar_venda()
        elif opcao == '10':
            os.system("cls")
            cancelar_compra()
        elif opcao == '11':
            os.system("cls")
            remover_produto()
        elif opcao == '12':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
            
def manuais():
    if autenticar():
        menu_principal()

if __name__ == "__main__":
    manuais()


