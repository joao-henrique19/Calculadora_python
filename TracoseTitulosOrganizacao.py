from Cores import Cores

def ColorirTexto(texto, coresin = Cores.RESET, coresfim = Cores.RESET):
    print(f'{coresin}{texto}{coresfim}')

def ColorirTitulosTracosOrganizacao(titulo,  qtd_tracos = 0, coresin = Cores.RESET, coresfim = Cores.RESET):
    print('-'*qtd_tracos)
    print(f'{coresin}{titulo:^{qtd_tracos}}{coresfim}')
    print('-'*qtd_tracos)

def TitulosTracosOrganizacao(titulo, qtd_tracos):
    print('-'*qtd_tracos)
    print(f'{titulo:^{qtd_tracos}}')
    print('-'*qtd_tracos)

def TracosOrganizacao(qtd_tracos):
    print('-'*qtd_tracos)
