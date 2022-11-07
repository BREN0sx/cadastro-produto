#Limpar terminal
import os


def clear():
    os.system("cls")

# Estilização
fb = '\033[93m'
fc = '\033[0;0m'
no_mark = '\n\033[31m'+"✖"
yes_mark = '\n\033[32m'+"✔"
plural = "s"

# Painel 
addProduct = fb+"=-=-=-= ADICIONAR PRODUTO =-=-=-="+fc
correctField = fb+"=-=-=-= CORRIGIR DADOS =-=-=-="+fc
consult = fb+"=-=-=-= CONSULTAR DADOS =-=-=-="+fc
delPanel = fb+"=-=-=-=-= LIMPAR DADOS =-=-=-=-="+fc
attField = fb+"=-=-=-= ATUALIZAR DADOS =-=-=-="+fc
endSlash = fb+("=-"*15)+"="+fc
subSlash = fb+("-"*31)+fc

noStock = "\n    Sem produto cadastrado\n"
backBtn = fb+"[ENTER] Voltar"+fc

dados = [[]]
name = ""; desc = ""; session = ""; stock = ""; price = ""
nameC = ""; descC = ""; sessionC = ""; stockC = ""; priceC = ""
while True:
    id = len(dados)
        
    clear()
    print(fb+"=-=-=-= PAINEL PRODUTO =-=-=-=")
    print('[1] Adicionar')
    print('[2] Consultar')
    print('[3] Atualizar')
    print('[4] Limpar')
    print('[0] Sair')
    print(endSlash)
    resp = input("Opção > ")
    
    if resp == "1":
        clear()
        print(addProduct)
        qp = int(input("\nQuantidade de produtos a ser adicionado: "))
        cont = 0
        while qp <= 0:
            clear()
            print(addProduct)
            print(no_mark, "Quantidade inválida", fc)
            qp = int(input("\nQuantidade de produtos a ser adicionado: "))
        while cont < qp:
            sn = ""
            clear()
            print(addProduct)
            print((" "*11)+fb+"CADASTRO", id, fc)
            dados.append([id, name, desc, session, stock, price])
            while dados[id][1] == "":
                name = input("Nome: ")
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            while dados[id][2] == "":
                desc = input("Descrição: ")
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            while dados[id][3] == "":
                session = input("Grupo: ")
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            while dados[id][4] == "":
                stock = int(input("Estoque: "))
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            while dados[id][5] == "":
                price = float(input("Preço: "))
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            print(endSlash)
            sn = input(fb+"[Enter] Confirmar | [C] Corrige"+fc+"\n> ")
            if (sn == "c" or sn == "C"):
                clear()
                print(correctField)
                print(fb+"\n[Enter] Não alterar\n"+fc)
                nameC = input("Nome(%s): " %name)
                descC = input("Descrição(%s): " %desc)
                sessionC = input("Grupo(%s): " %session)
                stockC = input("Estoque(%d): " %(int(stock) or 0))
                priceC = input("Preço(%.2f): " %(float(price) or 0))
                if nameC != "":
                   dados[id][1] = nameC
                if descC != "":
                   dados[id][2] = descC
                if sessionC != "":
                   dados[id][3] = sessionC
                if stockC != "":
                   dados[id][4] = int(stockC)
                if priceC != "":
                   dados[id][5] = float(priceC)
            name = ""; desc = ""; session = ""; stock = ""; price = ""
            nameC = ""; descC = ""; sessionC = ""; stockC = ""; priceC = ""
            cont += 1
            id += 1
        clear()
        print(addProduct)
        if (cont == 1):
            print(yes_mark, cont, "produto foi computado com sucesso"+fb)
        else:
            print(yes_mark, cont, "produtos foram computados com sucesso"+fb)
        print("\n"+endSlash)
        input(backBtn)
    elif resp == "2":
        clear()
        print(consult)
        print('[1] Consulta por ID')
        print('[2] Consulta Geral')
        print(endSlash)
        option = input("Opção > ")
        if option == "1":
            clear()
            print(consult)
            productId = int(input("ID: "))
            if (productId >= id) or (productId <= 0): 
                clear()
                print(consult)
                print(no_mark, "[%d] ID Inválido\n" %productId)
            else: 
                print("Nome:", dados[productId][1])
                print("Descrição:", dados[productId][2])
                print("Categoria:", dados[productId][3])
                print("Estoque: %d" %(dados[productId][4] or 0))
                print("Preço: R$%.2f" %(dados[productId][5] or 0))
            print(endSlash)
            input(backBtn)
        elif option == "2":
            clear()
            print(consult)
            if id == 1:
                print(noStock)
            else:
                cont = 1
                while id > cont:
                    print("ID:", cont)
                    print("Nome:", dados[cont][1])
                    print("Descrição:", dados[cont][2])
                    print("Categoria:", dados[cont][3])
                    print("Estoque: %d" %(dados[cont][4] or 0))
                    print("Preço: R$%.2f" %(dados[cont][5] or 0))
                    cont += 1
                    if (cont != id):
                       print(subSlash) 
            print(endSlash)
            input(backBtn)
        else:
            clear()
            print(consult)
            print(no_mark, "Opção inválida\n")
            print(endSlash)
            input(backBtn)
    elif resp == "3":
        clear()
        print(attField)
        if len(dados) == 1:
                print(noStock)
        else:
            productId = int(input(fc+"\nID do produto a atualizar: "))
            if (productId > id) or (productId <= 0): 
                print(no_mark, "ID Inválido")
            else:
                print(fb+"\n[Enter] Não alterar\n"+fc)
                nameA = input("Nome(%s): " %dados[productId][1])
                descA = input("Descrição(%s): " %dados[productId][2])
                sessionA = input("Grupo(%s): " %dados[productId][3])
                stockA = input("Estoque(%d): " %(dados[productId][4] or 0))
                priceA = input("Preço(%.2f): " %(dados[productId][5] or 0))
                if nameA != "":
                   dados[productId][1] = nameA
                if descA != "":
                   dados[productId][2] = descA
                if sessionA != "":
                   dados[productId][3] = sessionA
                if stockA != "":
                   dados[productId][4] = int(stockA)
                if priceA != "":
                   dados[productId][5] = float(priceA)
                if (priceA == "") and (stockA == "") and (sessionA == "") and (descA == "") and (nameA == ""):
                    print(no_mark, "Nenhum dado foi alterado")
                else:
                    print(yes_mark, "Dados fornecidos foram atualizados")
        print(endSlash)
        input(backBtn)
    elif resp == "4":
        clear()
        print(delPanel)
        if id == 1:
            print(noStock)
            print(endSlash)
            input(backBtn)
        else:
            print('[1] Limpar por ID')
            print('[2] Limpar Registros')
            print(endSlash)
            option = input("Opção > ")
            if option == "1":
                clear()
                print(delPanel)
                productId = int(input("ID: "))
                if (productId > id) or (productId <= 0): 
                    print(no_mark, "ID Inválido")
                    input(backBtn)
                else: 
                    print('[1] Limpar | Nome:', dados[productId][1])
                    print('[2] Limpar | Descrição:', dados[productId][2])
                    print('[3] Limpar | Grupo:', dados[productId][3])
                    print('[4] Limpar | Estoque: %d' %(dados[productId][4] or 0))
                    print('[5] Limpar | Preço: R$%.2f' %(dados[productId][5] or 0))
                    print('[6] Limpar Tudo')
                    print(endSlash)
                    optionDel = input("Opção > ")
                    clear()
                    print(delPanel)
                    if optionDel == "1":
                        dados[productId][1] = ""
                        print(yes_mark, "[ID %d] Nome, limpo com sucesso\n" %productId)
                    elif optionDel == "2":
                        dados[productId][2] = ""
                        print(yes_mark, "[ID %d] Descrição, limpo com sucesso\n" %productId)
                    elif optionDel == "3":
                        dados[productId][3] = ""
                        print(yes_mark, "[ID %d] Grupo, limpo com sucesso\n" %productId)
                    elif optionDel == "4":
                        dados[productId][4] = ""
                        print(yes_mark, "[ID %d] Estoque, limpo com sucesso\n" %productId)
                    elif optionDel == "5":
                        dados[productId][5] = ""
                        print(yes_mark, "[ID %d] Preço, limpo com sucesso\n" %productId)
                    elif optionDel == "6":
                        dados.pop(productId)
                        print(yes_mark, "[ID %d] Todos os campos foram limpos\n" %productId)
                    else:
                        print(no_mark, "Opção inválida\n")
                    print(endSlash)
                    input(backBtn)
            if option == "2":
                clear()
                print(delPanel)
                cont = 1
                while id > cont:
                    print("ID:", cont)
                    print("Nome:", dados[cont][1])
                    print("Descrição:", dados[cont][2])
                    print("Categoria:", dados[cont][3])
                    print("Estoque: %d" %(dados[cont][4] or 0))
                    print("Preço: R$%.2f" %(dados[cont][5] or 0))
                    cont += 1
                    if (cont != id):
                       print(subSlash) 
                if len(dados) == 2:
                    plural = ""
                print(endSlash)
                print("Prestes a remover: %d registro%s\n" % ((len(dados)-1), plural))
                print(fb+"[S] Prosseguir | [ENTER] Cancelar"+fc)
                confirm = input("> ")
                clear()
                print(delPanel)
                if confirm == "S" or confirm == "s":
                    print(yes_mark, "%d registro%s removido%s\n" % ((len(dados)-1), plural, plural))
                    dados = [[]]
                else: 
                    print(yes_mark, "Ação cancelada\n")
                print(endSlash)
                input(backBtn)
    elif resp == "0":
        clear()
        print(resp)
        print(fb+"[ENTER] Sair | [C] Cancelar"+fc)
        respf = input("> ")
        if (respf == "c") or (respf == "C"):
            clear()
        else:
            clear()
            print(yes_mark, "Programa finalizado"+fc)
            break
