# type: ignore

import os # >> https://docs.python.org/3/library/os.html#os.system
fb, fc, no_mark, yes_mark, plural = ('\033[93m', '\033[0;0m', '\n\033[31m'+"✖", '\n\033[32m'+"✔", "s")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuTitle(name):
    if name == "add":
        print(fb+("=-=-=-= ADICIONAR PRODUTO =-=-=-=")+fc)
    elif name == "revise":
        print(fb+"=-=-=-= CORRIGIR DADOS =-=-=-="+fc)
    elif name == "del":
        print(fb+"=-=-=-=-= LIMPAR DADOS =-=-=-=-="+fc)
    elif name == "read":
        print(fb+"=-=-=-= CONSULTAR DADOS =-=-=-="+fc)
    elif name == "update":
        print(fb+"=-=-=-= ATUALIZAR DADOS =-=-=-="+fc)
    elif name == "main":
        print(fb+"=-=-=-= PAINEL PRODUTO =-=-=-=")
        print('[1] Adicionar')
        print('[2] Consultar')
        print('[3] Atualizar')
        print('[4] Limpar')
        print('[0] Sair')
    else:
        return

def menuFields(dados, productId):
    print("Nome:", dados[productId][1].capitalize())
    print("Descrição:", dados[productId][2].capitalize())
    print("Categoria:", dados[productId][3].capitalize())
    print("Estoque: %d" %(dados[productId][4] or 0))
    print("Preço: R$%.2f" %(dados[productId][5] or 0))

def menuFooter(name):
    if name == "end":
        print(fb+("=-"*15)+"="+fc)
    elif name == "sub":
        print(fb+("-"*31)+fc)
    else:
        return

def plural(l):
    if ((len(l)-1) <= 1):
        return ""
    else:
        return "s"

def removedIDs(dados):
    rep, nb = (0, 0)
    dadosLen = int(len(dados))-1
    for cont in dados:
        if (cont != []) and (cont != [rep]):
            nb += 1
        if ((dadosLen-1) == rep):
            return nb+1
        rep += 1

def rtnValue(value, type):
    try: # >> https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        if type == 1:
            return int(value)
        if type == 2:
            return float(value)
    except ValueError:
        return 0
