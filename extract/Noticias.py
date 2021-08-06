import re
from unidecode import unidecode
import util.loadDados as gravaDados
import os
import pandas as pd

def noticias(soup):
    # Pegando as linhas da tabela 
    info = soup.find_all(id="id_news")

    # Tratando os dados
    cont = 0
    lista = []
    for x in info:
        x = str(x)
        limpo = x.replace('</tr>','')
        clean = re.compile('<tr.*?>')
        limpo = re.sub(clean, '|', limpo)
        clean = re.compile('<a href="')
        limpo = re.sub(clean, '#', limpo)
        
        clean = re.compile('<th.*?>.*?</th>')
        limpo = re.sub(clean, '', limpo)
        clean = re.compile('<td.*?>')
        limpo = re.sub(clean, '#', limpo)
        limpo = limpo.replace('</td>', '#')
        clean = re.compile('<.*?>')
        limpo = re.sub(clean, '', limpo)
        limpo = limpo.replace('\n', '').replace('\xa0','')
        limpo = limpo.replace('[', '')
        limpo = limpo.replace(']', '')
        limpo = limpo.replace('">', '#')
        limpo = limpo.replace('#|#', '@')
        limpo = limpo.replace('##', '#')
        limpo = limpo.replace('|', '')
        limpo = unidecode(limpo)
        listLinhas = limpo.split('@')

        for lista in listLinhas:
            listal = lista.split('#')
            while '' in listal:
                listal.remove('')
            # Tranformando o dado em Json
            strData = listal[0].split('/')
            dataArq = str(strData[2])+str(strData[1])+str(strData[0])
            nomeArq = 'noticias'+dataArq+'.json'

            regFromula = re.compile('\/\/')
            strLink = re.sub(regFromula, 'https://', listal[3])

            dfForum = pd.DataFrame()

            json = {	
                "Data":dataArq,
                "Hora":listal[1],
                "Fonte":listal[2],
                "Noticias":listal[4],
                "Link":strLink
            }

            if os.path.exists('.dados/noticias/'+nomeArq):
                arquivo = pd.read_json('./dados/noticia/'+nomeArq)
                if listal[0] not in arquivo["Data"].values and listal[3] not in arquivo['Noticia'].values:
                    # Tranformando o Json em Dataframe
                    dfForum = arquivo
                    dfForum = dfForum.append(json,ignore_index=True)
                    gravaDados.persiste('noticias', dfForum, nomeArq)
            else:
                # Tranformando o Json em Dataframe
                dfForum = dfForum.append(json,ignore_index=True)
                gravaDados.persiste('noticias', dfForum, nomeArq)
