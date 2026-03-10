from TracoseTitulosOrganizacao import TracosOrganizacao
from TracoseTitulosOrganizacao import ColorirTexto
from Cores import Cores

def EntradaNumeros():
    qtd_numeros = str(input('Digite a quantidade de números para operar: '))
    TracosOrganizacao(70)
    while qtd_numeros.isnumeric() == False:
        ColorirTexto('Error, digite apenas quantidades inteiras.', Cores.VERMELHO, Cores.RESET)
        TracosOrganizacao(70)
        qtd_numeros = str(input('Digite a quantidade de números para operar: '))
        TracosOrganizacao(70)

    qtd_numeros = int(qtd_numeros)

    lista_numeros = []
    for numero in range(0, qtd_numeros):
        num = str(input(f'Digite o {numero+1}° número: '))
        while num.replace('.', '').isnumeric() == False:
            TracosOrganizacao(70)
            ColorirTexto('Error, digite apenas números.', Cores.VERMELHO, Cores.RESET)
            TracosOrganizacao(70)
            num = str(input(f'Digite o {numero+1}° número: '))

        lista_numeros.append(float(num))
    return lista_numeros

def EntradaBasePotencia():
    base = str(input('Digite a base:  '))
    while base.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas númeors inteiros.', Cores.VERMELHO, Cores.RESET)
        TracosOrganizacao(70)
        base = str(input('Digite a base:  '))
        TracosOrganizacao(70)

    return int(base)

def EntradaExpoente():
    expoente = str(input('Digite o expoente: '))
    while expoente.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas números inteiros.', Cores.VERMELHO, Cores.RESET)
        TracosOrganizacao(70)
        expoente = str(input('Digite o expoente: '))
        TracosOrganizacao(70)

    return int(expoente)

def EntradaNumFatorial():
    num_fatorial = str(input('Digite um número: '))
    while num_fatorial.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas números inteiros.', Cores.VERMELHO, Cores.RESET)
        TracosOrganizacao(70)
        num_fatorial = str(input('Digite um número: '))
        TracosOrganizacao(70)
    num_fatorial = int(num_fatorial)
    return num_fatorial

def EntradaSenCosTan():
    valor_unico = str(input('Digite um número: '))
    while valor_unico.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas números inteiros.', Cores.VERMELHO, Cores.RESET)
        TracosOrganizacao(70)
        valor_unico = str(input('Digite um número: '))
        TracosOrganizacao(70)

    return int(valor_unico)

def EntradaRaiz():
    num = str(input('Digite um número: √'))
    while num.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas números inteiros.', Cores.VERMELHO, Cores.RESET) 
        TracosOrganizacao(70)
        num = str(input('Digite um número: √'))
        TracosOrganizacao(70)

    return int(num)

def EntradaLogNum():
    num = str(input('Digite um número: '))
    while num.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas números inteiros.', Cores.VERMELHO, Cores.RESET) 
        TracosOrganizacao(70)
        num = str(input('Digite um número: '))
        TracosOrganizacao(70)

    return int(num)

def BaseLog():
    num = str(input('Digite a base: '))
    while num.isnumeric() == False:
        TracosOrganizacao(70)
        ColorirTexto('Error, digite apenas números inteiros.', Cores.VERMELHO, Cores.RESET) 
        TracosOrganizacao(70)
        num = str(input('Digite a base: '))
        TracosOrganizacao(70)

    return int(num)