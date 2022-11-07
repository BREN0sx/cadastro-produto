clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n"
fb = '\033[30m'
fc = '\033[0;0m'
no_mark = '\n\033[31m'+"✖"
yes_mark = '\n\033[32m'+"✔"

resp = 6

nome = ''
desc = ''
grupo = ''
stock = ''
valor = ''

nomeC = ''
descC = ''
grupoC = ''
stockC = ''
valorC = ''
while resp != '':
    print("\n"+fb+"=-=-=-= PAINEL PRODUTO =-=-=-=")
    print('[1] Adicionar')
    print('[2] Consultar')
    print('[3] Atualizar')
    print('[4] Limpar')
    print('[0] Sair')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="+fc)
    resp = input("Opção > ")
    if resp == "1":
        print(clear)
        print("\n"+fb+"=-=-=-= ADICIONAR PRODUTO =-=-=-=\n"+fc)
        while nome == "":
            nome = input("Nome: ")
        while desc == "":
            desc = input("Descrição: ")
        while grupo == "":
            grupo = input("Grupo: ")
        stock = input("Estoque: ")
        while valor == '':
            valor = input("Preço: ")
        if stock != '':
            stock = int(stock)
        if valor != '':
            valor = float(valor)

        sn = input(fb+"\n[Enter] Confirmar\n[C] Corrigir"+fc+"\nAção > ")
        if (sn == "c" or sn == "C"):
            print(clear)
            print("\n"+fb+"=-=-=-= CORRIGIR DADOS =-=-=-=\n")
            print("[Enter] Não alterar\n"+fc)
            if nomeC == "":
                nomeC = input("Nome(%s): " %nome)
            if descC == "":
                descC = input("Descrição(%s): " %desc)
            if grupoC == "":
                grupoC = input("Grupo(%s): " %grupo)
            if stockC == '':
                stockC = input("Estoque(%d): " %(int(stock) or 0))
            if valorC == '':
                valorC = input("Preço(%.2f): " %(float(valor) or 0))
            checkcor = yes_mark+" Correção aplicada com sucesso"
            if nomeC != '':
                nome = nomeC
                print(checkcor)
            if descC != '':
                desc = descC
                print(checkcor)
            if grupoC != '':
                grupo = grupoC
                print(checkcor)
            if stockC != '':
                stock = int(stockC)
                print(checkcor)
            if valorC != '':
                valor = float(valorC)
                print(checkcor)
            if nomeC == '' and descC == '' and grupoC == '' and stockC == '' and valorC == '':
                print(no_mark, "Não foi feita nenhuma correção")
            print(yes_mark+" Produto computado com sucesso")
    elif resp == "2":
        print(clear)
        print("\n"+fb+"=-=-=-= CONSULTAR DADOS =-=-=-=")
        if nome == '' and desc == '' and grupo == '' and stock == '' and valor == '':
            print("\nSem produto cadastrado\n")
        else:
            print('Nome:', nome)
            print('Descrição:', desc)
            print('Grupo:', grupo)
            print('Estoque: %d' %(stock or 0))
            print('Preço: R$%.2f' %(valor or 0))
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        input("[ENTER] Voltar "+fc)
    elif resp == "3":
        print(clear)
        print("\n"+fb+"=-=-=-= ATUALIZAR DADOS =-=-=-=\n")
        if nome == '' and desc == '' and grupo == '' and stock == '' and valor == '':
            print("Sem produto cadastrado\n")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            input("[ENTER] Voltar "+fc)
        else:
            print("[Enter] Não alterar\n"+fc)
            nomeA = input("Nome(%s): " %nome)
            descA = input("Descrição(%s): " %desc)
            grupoA = input("Grupo(%s): " %grupo)
            stockA = input("Estoque(%d): " %(int(stock) or 0))
            valorA = input("Preço(R$%.2f): " %(float(valor) or 0))
            checkcor = yes_mark+" Dados fornecidos foram atualizados com sucesso"
            if nomeA != '':
                nome = nomeA
                print(checkcor)
            elif descA != '':
                desc = descA
                print(checkcor)
            elif grupoA != '':
                grupo = grupoA
                print(checkcor)
            elif stockA != '':
                stock = int(stockA)
                print(checkcor)
            elif valorA != '':
                valor = float(valorA)
                print(checkcor)
            else: 
                print(no_mark, "Não foi feita nenhuma atualização nos dados")
    elif resp == "4":
        print(clear)
        if nome == '' and desc == '' and grupo == '' and stock == '' and valor == '':
            print("\n"+fb+"=-=-=-= LIMPAR DADOS =-=-=-=\n")
            print("Sem produto cadastrado\n")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            input("[ENTER] Voltar "+fc)
        else:
            print("\n"+fb+"=-=-=-= LIMPAR DADOS =-=-=-=\n")
            print('[1] Limpar | Nome:', nome)
            print('[2] Limpar | Descrição:', desc)
            print('[3] Limpar | Grupo:', grupo)
            print('[4] Limpar | Estoque: %d' %(float(stock) or stock or 0))
            print('[5] Limpar | Preço: R$%.2f' %(float(valor) or valor or 0))
            print('[6] Limpar Tudo')
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="+fc)
            resp2 = input("Opção > ")
            if resp2 == "1":
                nome = ''
                print(yes_mark, "Nome, limpo com sucesso")
            elif resp2 == "2":
                desc = ''
                print(yes_mark, "Descrição, limpo com sucesso")
            elif resp2 == "3":
                grupo = ''
                print(yes_mark, "Grupo, limpo com sucesso")
            elif resp2 == "4":
                stock = 0
                print(yes_mark, "Estoque, limpo com sucesso")
            elif resp2 == "5":
                valor = 0
                print(yes_mark, "Preço, limpo com sucesso")
            elif resp2 == "6":
                nome = ''
                desc = ''
                grupo = ''
                stock = 0
                valor = 0
                print(yes_mark, "Todos os campos foram limpos com sucesso")
            else:
                print(no_mark,"Opção inválida")
    elif resp == "0":
        resp3 = input("Clique [ENTER] para sair, para cancelar a ação tecle [c]")
        if resp3 == "c" or resp3 == "C":
            print(yes_mark, "Ação cancelada")
        else:
            print(yes_mark, "Programa finalizado")
            break
    else:
        print(no_mark, "Opção inválida")
