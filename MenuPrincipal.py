# Autor: João Henrique Peixoto Viana de Oliveira

from TracoseTitulosOrganizacao import TracosOrganizacao, ColorirTitulosTracosOrganizacao, ColorirTexto, TitulosTracosOrganizacao
from Cores import Cores

def MenuPrincipal():
    ColorirTitulosTracosOrganizacao('MENU CALCULADORA', 70, Cores.AZUL, Cores.RESET)
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potência')
    print('6 - Raiz quadrada')
    print('7 - Seno')
    print('8 - Cosseno')
    print('9 - Tangente')
    print('10 - Logaritimo')
    print('11 - Fatorial')
    print('12 - Sair')
    TracosOrganizacao(70)
    