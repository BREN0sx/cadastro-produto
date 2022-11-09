#Limpar terminal
import defs

# Estilização
fb = '\033[93m'
fc = '\033[0;0m'
no_mark = '\n\033[31m'+"✖"
yes_mark = '\n\033[32m'+"✔"
plural = "s"

noStock = "\n    Sem produto cadastrado\n"
backBtn = fb+"[ENTER] Voltar"+fc

dados = [[]]
name = ""; desc = ""; session = ""; stock = ""; price = ""
nameC = ""; descC = ""; sessionC = ""; stockC = ""; priceC = ""
while True:
    id = len(dados)
        
    defs.clear()
    defs.menuTitle("main")
    defs.menuFooter("end")
    resp = input("Opção > ")
    
    if resp == "1":
        defs.clear()
        defs.menuTitle("add")
        qp = int(input("\nQuantidade de produtos a ser adicionado: "))
        cont = 0
        while qp <= 0:
            defs.clear()
            defs.menuTitle("add")
            print(no_mark, "Quantidade inválida", fc)
            qp = int(input("\nQuantidade de produtos a ser adicionado: "))
        while cont < qp:
            sn = ""
            defs.clear()
            defs.menuTitle("add")
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
            defs.menuFooter("end")
            sn = input(fb+"[Enter] Confirmar | [C] Corrige"+fc+"\n> ")
            if (sn == "c" or sn == "C"):
                defs.clear()
                defs.menuTitle("revise")
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
        defs.clear()
        defs.menuTitle("add")
        if (cont == 1):
            print(yes_mark, cont, "produto foi computado com sucesso\n"+fb)
        else:
            print(yes_mark, cont, "produtos foram computados com sucesso\n"+fb)
        defs.menuFooter("end")
        input(backBtn)
    elif resp == "2":
        defs.clear()
        defs.menuTitle("read")
        print('[1] Consulta por ID')
        print('[2] Consulta Geral')
        defs.menuFooter("end")
        option = input("Opção > ")
        if option == "1":
            defs.clear()
            defs.menuTitle("read")
            productId = int(input("ID: "))
            if (productId >= id) or (productId <= 0): 
                defs.clear()
                defs.menuTitle("read")
                print(no_mark, "[%d] ID Inválido\n" %productId)
            else: 
                defs.menuFields(dados, productId)
            defs.menuFooter("end")
            input(backBtn)
        elif option == "2":
            defs.clear()
            defs.menuTitle("read")
            if id == 1:
                print(noStock)
            else:
                cont = 1
                while id > cont:
                    print("ID:", cont)
                    defs.menuFields(dados, cont)
                    cont += 1
                    if (cont != id):
                       defs.menuFooter("sub") 
            defs.menuFooter("end")
            input(backBtn)
        else:
            defs.clear()
            defs.menuTitle("read")
            print(no_mark, "Opção inválida\n")
            defs.menuFooter("end")
            input(backBtn)
    elif resp == "3":
        defs.clear()
        defs.menuTitle("update")
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
        defs.menuFooter("end")
        input(backBtn)
    elif resp == "4":
        defs.clear()
        defs.menuTitle("del")
        if id == 1:
            print(noStock)
            defs.menuFooter("end")
            input(backBtn)
        else:
            print('[1] Limpar por ID')
            print('[2] Limpar Registros')
            defs.menuFooter("end")
            option = input("Opção > ")
            if option == "1":
                defs.clear()
                defs.menuTitle("del")
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
                    defs.menuFooter("end")
                    optionDel = input("Opção > ")
                    defs.clear()
                    defs.menuTitle("del")
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
                    defs.menuFooter("end")
                    input(backBtn)
            if option == "2":
                defs.clear()
                defs.menuTitle("del")
                cont = 1
                while id > cont:
                    print("ID:", cont)
                    defs.menuFields(dados, cont)
                    cont += 1
                    if (cont != id):
                       defs.menuFooter("sub") 
                if len(dados) == 2:
                    plural = ""
                defs.menuFooter("end")
                print("Prestes a remover: %d registro%s\n" % ((len(dados)-1), plural((len(dados)-1),"s")))
                print(fb+"[S] Prosseguir | [ENTER] Cancelar"+fc)
                confirm = input("> ")
                defs.clear()
                defs.menuTitle("del")
                if confirm == "S" or confirm == "s":
                    print(yes_mark, "%d registro%s removido%s\n" % ((len(dados)-1), plural, plural))
                    dados = [[]]
                else: 
                    print(yes_mark, "Ação cancelada\n")
                defs.menuFooter("end")
                input(backBtn)
    elif resp == "0":
        defs.clear()
        print(resp)
        print(fb+"[ENTER] Sair | [C] Cancelar"+fc)
        respf = input("> ")
        if (respf == "c") or (respf == "C"):
            defs.clear()
        else:
            defs.clear()
            print(yes_mark, "Programa finalizado"+fc)
            break