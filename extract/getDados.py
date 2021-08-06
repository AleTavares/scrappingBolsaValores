from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
# import requests

def getScraping(url):
    # Abre a conexão com a url
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()

    # Extrai o código HTML
    soup = bs(html,'lxml')

    return soup


