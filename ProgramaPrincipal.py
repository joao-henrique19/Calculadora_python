from MenuPrincipal import MenuPrincipal
from Escolhas import OperacaoEscolhida
from TracoseTitulosOrganizacao import TracosOrganizacao, TitulosTracosOrganizacao

def Main():
    continuar = 'S'
    while continuar.upper() == 'S':
        MenuPrincipal()

        operacao = input('Operação: ').strip()
        TracosOrganizacao(70)
        OperacaoEscolhida(operacao)
        if operacao == '12':
            TitulosTracosOrganizacao('FIM DO PROGRAMA', (70))
            break

Main()
