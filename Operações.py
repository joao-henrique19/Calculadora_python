from Formatações import *
from TracoseTitulosOrganizacao import TracosOrganizacao
from math import sqrt, sin, cos, tan, radians, log

def soma(EntradaNumeros):
    soma = 0
    for numero in EntradaNumeros:
        soma += numero
    TracosOrganizacao(70)
    return f'O resultado da soma de {EntradaNumeros} = {soma:.2f}'

def subtracao(EntradaNumeros):
    for indice, numero in enumerate(EntradaNumeros):
        if indice == 0:
            subtracao = numero
        else:
            subtracao -= numero
    TracosOrganizacao(70)
    return f'O resultado da subtração de {EntradaNumeros} = {subtracao:.2f}'

def multiplicacao(EntradaNumeros):
    multiplicacao = 1
    for numero in EntradaNumeros:
        multiplicacao *= numero
    TracosOrganizacao(70)
    return f'O resultado da multiplicação de {EntradaNumeros} = {multiplicacao:.2f}'


def divisao(EntradaNumeros):
    try:
        for indice, numero in enumerate(EntradaNumeros):
            if indice == 0:
                divisao = numero
            else:
                divisao /= numero
        TracosOrganizacao(70)
        return f'O resultado da divisão de {EntradaNumeros} = {divisao:.2f}'
    
    except ZeroDivisionError:
        TracosOrganizacao(70)
        return 'Não foi possível efetuar a divisão por zero'

def potencia(Entradabase, entradaexpoente):
    
    base = Entradabase
    expoente = entradaexpoente
    potenciacao = base ** expoente

    TracosOrganizacao(70)
    return f'O resultado de {base}{sobrescrito(expoente)} = {potenciacao}'

def raizquadrada(EntradaRaiz):
    if EntradaRaiz < 0:
        TracosOrganizacao(70)
        return 'Não existe raiz quadrada real de número negativo.'

    raiz = sqrt(EntradaRaiz)

    TracosOrganizacao(70)
    return f'A √{EntradaRaiz} = {raiz:.2f}'

def seno(EntradaSin):
    seno = sin(radians(EntradaSin))

    TracosOrganizacao(70)
    return f'O seno de {EntradaSin}° = {seno:.2f}.'

def cosseno(EntradaCos):
    cosseno = cos(radians(EntradaCos))

    TracosOrganizacao(70)
    return f'O cosseno de {EntradaCos}° = {cosseno:.2f}.'

def tangente(EntradaTan):
    if EntradaTan % 90 == 0 and EntradaTan % 180 != 0:
        TracosOrganizacao(70)
        return 'Tangente indefinida para esse ângulo.'

    tangente = tan(radians(EntradaTan))

    TracosOrganizacao(70)
    return f'A tangente de {EntradaTan}° = {tangente:.2f}'

def logaritimo(LogDeNum, base):
    if LogDeNum <= 0:
        TracosOrganizacao(70)
        return 'O logaritmo só existe para números maiores que zero.'

    if base <= 0 or base == 1:
        TracosOrganizacao(70)
        return 'Base de logaritmo inválida.'

    logaritimo = log(base, LogDeNum)

    TracosOrganizacao(70)
    return f'Log{LogDeNum}({base}) = {logaritimo:.2f}'

def fatorial(EntradaNumeroFatorial):
    TracosOrganizacao(70)
    print(f'O fatorial de {EntradaNumeroFatorial}: ')
    TracosOrganizacao(70)
    
    fatorial = 1
    for i in range(EntradaNumeroFatorial, 0, -1):
        fatorial *= i
        print(i, end='')
        if i > 1:
            print(' x ', end='')
        else:
            print(' =', fatorial)
    
