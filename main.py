import sys

from numpy.lib.function_base import extract 
import extract.getDados as getDados
import extract.Cotacoes as getCotacao
import extract.Balanco as getBalanco
import extract.Forum as getForuns
import extract.Noticias as getNoticias
print()

if __name__ == '__main__':
    dadosColetados = getDados.getScraping('https://br.advfn.com/bolsa-de-valores/bovespa/enjoei-on-ENJU3/cotacao')
    # print (dadosColetados)

    if len(sys.argv) > 1:
        for param in sys.argv:
            if param == 'cotacaes': # esta dando erro de indice
                getCotacao.cotacao(dadosColetados) 
            elif param == 'balancos':
                getBalanco.balanco(dadosColetados)
            elif param == 'foruns':
                getForuns.forum (dadosColetados)
            elif param == 'noticias':
                getNoticias.noticias(dadosColetados)
    else:
        getCotacao.cotacao(dadosColetados) 
        getBalanco.balanco(dadosColetados)
        getForuns.forum (dadosColetados)
        getNoticias.noticias(dadosColetados)
