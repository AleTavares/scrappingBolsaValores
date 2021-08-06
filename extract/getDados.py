# DESCRIÇÂO: Este módulo  scraping da pagina informada no parametro url

# Importação dos modulos necessarios para a coleta dos dados
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

def getScraping(url):
    # Abre a conexão com a url
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()

    # Extrai o código HTML
    soup = bs(html,'lxml')

    # retorna o codigo html extraido
    return soup


