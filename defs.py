import os


fb = '\033[93m'
fc = '\033[0;0m'
no_mark = '\n\033[31m'+"✖"
yes_mark = '\n\033[32m'+"✔"
plural = "s"

def clear():
    os.system("cls")

def menuTitle(name):
    if name == "add":
        print(fb+"=-=-=-= ADICIONAR PRODUTO =-=-=-="+fc)
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
    print("Nome:", dados[productId][1])
    print("Descrição:", dados[productId][2])
    print("Categoria:", dados[productId][3])
    print("Estoque: %d" %(dados[productId][4] or 0))
    print("Preço: R$%.2f" %(dados[productId][5] or 0))
def menuFooter(name):
    if name == "end":
        print(fb+("=-"*15)+"="+fc)
    elif name == "sub":
        print(fb+("-"*31)+fc)
    else:
        return
def plural(l, rtn):
    if (l <= 1):
        return
    else:
        return rtn