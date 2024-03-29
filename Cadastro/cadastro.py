# type: ignore >> https://mypy.readthedocs.io/en/stable/common_issues.html#ignoring-a-whole-file

import defs
fb, fc, no_mark, yes_mark, plural = ('\033[93m', '\033[0;0m', '\n\033[31m'+"✖", '\n\033[32m'+"✔", "s") 
noStock = "\n    Sem produto cadastrado\n"; backBtn = fb+"[ENTER] Voltar"+fc

ler_cadastro = open("dados.txt", 'r', encoding="utf-8")
dados = eval(ler_cadastro.read()) # >> https://docs.python.org/3/library/functions.html#eval

name, desc, session, stock, price = ("", "", "", "", "")
nameC, descC, sessionC, stockC, priceC = ("", "", "", "", "")

while True:
    id = len(dados)

    defs.clear()
    defs.menuTitle("main")
    defs.menuFooter("end")
    resp = input("Opção > ")
    
    if resp == "1":
        defs.clear()
        defs.menuTitle("add")
        cont, qp = (0,0)
        while qp <= 0:
            qp = input("\nQuantidade de produtos a ser adicionado: ")
            qp = defs.rtnValue(qp, 1)
            if qp <= 0:
                qp = 1
        while cont < qp:
            sn = ""
            defs.clear()
            defs.menuTitle("add")
            print(fb, ("CADASTRO ID %s" %id).center(30), fc)
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
                stock = input("Estoque: ")
                stock = defs.rtnValue(stock, 1)
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            while dados[id][5] == "":
                price = input("Preço: ")
                price = defs.rtnValue(price, 2)
                dados.pop(-1)
                dados.append([id, name, desc, session, stock, price])
            defs.menuFooter("end")
            sn = input(fb+"[Enter] Confirmar | [C] Corrige"+fc+"\n> ")
            if sn.lower() == "c": # >> https://docs.python.org/3/library/stdtypes.html#str.lower
                defs.clear()
                defs.menuTitle("revise")
                print(fb+"\n[Enter] Não alterar\n"+fc)
                nameC = input("Nome(%s): " %name.capitalize()) # >> https://docs.python.org/3/library/stdtypes.html#str.capitalize
                descC = input("Descrição(%s): " %desc.capitalize())
                sessionC = input("Grupo(%s): " %session.capitalize())
                stockC = input("Estoque(%d): " %(int(stock) or 0))
                priceC = input("Preço(%.2f): " %(float(price) or 0))
                if nameC != "":
                   dados[id][1] = nameC
                if descC != "":
                   dados[id][2] = descC
                if sessionC != "":
                   dados[id][3] = sessionC
                if stockC != "":
                   dados[id][4] = defs.rtnValue(stockC, 1)
                if priceC != "":
                   dados[id][5] = defs.rtnValue(priceC, 2)
            name, desc, session, stock, price = ("", "", "", "", "")
            nameC, descC, sessionC, stockC, priceC = ("", "", "", "", "")
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
            productId = input("ID: ")
            productId = defs.rtnValue(productId, 1)
            if (productId >= id) or (productId <= 0) or (dados[productId] == [productId]): 
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
            if defs.removedIDs(dados) == 0 or defs.removedIDs(dados) == None:
                print(noStock)
            else:
                cont = 1
                while id > cont:
                    if (dados[cont] != [cont]):
                        print("ID:", cont)
                        defs.menuFields(dados, cont)
                    cont += 1
                    if (cont != id) and (dados[cont] != [cont]):
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
        if defs.removedIDs(dados) == 0 or defs.removedIDs(dados) == None:
                print(noStock)
        else:
            productId = input(fc+"\nID do produto a atualizar: ")
            productId = defs.rtnValue(productId, 1)
            if (productId >= id) or (productId <= 0) or (dados[productId] == [productId]): 
                print(no_mark, "[%d] ID Inválido\n" %productId)
            else:
                print(fb+"\n[Enter] Não alterar\n"+fc)
                nameA = input("Nome(%s): " %dados[productId][1].capitalize())
                descA = input("Descrição(%s): " %dados[productId][2].capitalize())
                sessionA = input("Grupo(%s): " %dados[productId][3].capitalize())
                stockA = input("Estoque(%d): " %(dados[productId][4] or 0))
                priceA = input("Preço(%.2f): " %(dados[productId][5] or 0))
                if nameA != "":
                   dados[productId][1] = nameA
                if descA != "":
                   dados[productId][2] = descA
                if sessionA != "":
                   dados[productId][3] = sessionA
                if stockA != "":
                   dados[productId][4] = defs.rtnValue(stockA, 1)
                if priceA != "":
                   dados[productId][5] = defs.rtnValue(priceA, 2)
                if (priceA == "") and (stockA == "") and (sessionA == "") and (descA == "") and (nameA == ""):
                    print(no_mark, "Nenhum dado foi alterado")
                else:
                    print(yes_mark, "Dados fornecidos foram atualizados")
        defs.menuFooter("end")
        input(backBtn)
    elif resp == "4":
        defs.clear()
        defs.menuTitle("del")
        if defs.removedIDs(dados) == 0 or defs.removedIDs(dados) == None:
            
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
                productId = input("ID: ")
                productId = defs.rtnValue(productId, 1)
                if (productId >= id) or (productId <= 0) or (dados[productId] == [productId]): 
                    print(no_mark, "[%d] ID Inválido\n" %productId)
                    input(backBtn)
                else: 
                    print('[1] Limpar | Nome:', dados[productId][1].capitalize())
                    print('[2] Limpar | Descrição:', dados[productId][2].capitalize())
                    print('[3] Limpar | Grupo:', dados[productId][3].capitalize())
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
                        dados[productId] = [productId]
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
                    if (dados[cont] != [cont]):
                        print("ID:", cont)
                        defs.menuFields(dados, cont)
                    cont += 1
                    if (cont != id) and (dados[cont] != [cont]):
                       defs.menuFooter("sub") 
                defs.menuFooter("end")
                print("Prestes a remover: %d registro%s\n" % (defs.removedIDs(dados), defs.plural(dados)))
                print(fb+"[S] Prosseguir | [ENTER] Cancelar"+fc)
                confirm = input("> ")
                defs.clear()
                defs.menuTitle("del")
                if confirm.lower() == "s":
                    print(yes_mark, "%d registro%s removido%s\n" % (defs.removedIDs(dados), defs.plural(dados), defs.plural(dados)))
                    dados = [[]]
                else: 
                    print(yes_mark, "Ação cancelada\n")
                defs.menuFooter("end")
                input(backBtn)
    elif resp == "0":
        defs.clear()
        print(fb+"[ENTER] Sair | [C] Cancelar"+fc)
        respf = input("> ")
        if respf.lower() == "c":
            defs.clear()
        else:
            defs.clear()
            print(yes_mark, "Programa finalizado"+fc)
            break
    ler_cadastro.close()        
    arquivo_cadastro = open("dados.txt", 'w+', encoding="utf-8")
    arquivo_cadastro.write("%s" %dados)
    arquivo_cadastro.close()
