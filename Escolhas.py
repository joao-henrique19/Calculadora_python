from TracoseTitulosOrganizacao import TracosOrganizacao, ColorirTexto, TitulosTracosOrganizacao
from Cores import Cores
from Operações import *
from EntradaNumerosOperacoes import *

def OperacaoEscolhida(opcao):
    while not opcao.isnumeric() or opcao not in ('1','2','3','4','5','6','7','8','9','10','11','12'):
        ColorirTexto('Operação inválida, tente novamente.', Cores.VERMELHO, Cores.RESET)
        TracosOrganizacao(70)
        opcao = input('Operação: ').strip()
        TracosOrganizacao(70)

    else:
        opcao = int(opcao)
        if opcao == 1:
           print('ADIÇÃO')
           TracosOrganizacao(70)
           print(soma(EntradaNumeros()))
           TracosOrganizacao(70)
        
        elif opcao == 2:
            print('SUBTRAÇÃO')
            TracosOrganizacao(70)
            print(subtracao(EntradaNumeros()))
            TracosOrganizacao(70)

        elif opcao == 3:
            print('MULTIPLICAÇÃO')
            TracosOrganizacao(70)
            print(multiplicacao(EntradaNumeros()))
            TracosOrganizacao(70)

        elif opcao == 4:
            print('DIVISÃO')
            TracosOrganizacao(70)
            print(divisao(EntradaNumeros()))
            TracosOrganizacao(70)

        elif opcao == 5:
            print('POTÊNCIA')
            TracosOrganizacao(70)
            print(potencia(EntradaBasePotencia(), EntradaExpoente()))
            TracosOrganizacao(70)

        elif opcao == 6:
            print('RAIZ QUADRADA')
            TracosOrganizacao(70)
            print(raizquadrada(EntradaRaiz()))
            TracosOrganizacao(70)

        elif opcao == 7:
            print('SENO')
            TracosOrganizacao(70)
            print(seno(EntradaSenCosTan()))
            TracosOrganizacao(70)

        elif opcao == 8:
            print('COSSENO')
            TracosOrganizacao(70)
            print(cosseno(EntradaSenCosTan())) 
            TracosOrganizacao(70)

        elif opcao == 9:
            print('TANGENTE')
            TracosOrganizacao(70)
            print(tangente(EntradaSenCosTan()))
            TracosOrganizacao(70)

        elif opcao == 10:
            print('LOGARITIMO')
            TracosOrganizacao(70)
            print(logaritimo(EntradaLogNum(), BaseLog()))

        elif opcao == 11:
            print('FATORIAL')
            TracosOrganizacao(70)
            fatorial(EntradaNumFatorial())
            TracosOrganizacao(70)
