import re
from unidecode import unidecode
import util.loadDados as gravaDados
import os
import pandas as pd

def forum(soup):
    # Pegando as linhas da tabela 
    info = soup.find_all(id="id_threads")

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
        
            strData = listal[0].split('/')
            dataArq = str(strData[2])+str(strData[1])+str(strData[0])
            nomeArq = 'forum'+dataArq+'.json'
            # Tranformando o dado em Json

            dfForum = pd.DataFrame()
            regFromula = re.compile('\/\/')
            strLink = re.sub(regFromula, 'https://', listal[3])
            json = {
                "Data":dataArq,
                "Hora":listal[1],
                "Comentarios":listal[2],
                "Discussao":listal[4],
                "Link": strLink
            }
            if os.path.exists('./dados/forum/'+nomeArq):
                arquivo = pd.read_json('./dados/forum/'+nomeArq)
                if listal[0] not in arquivo["Data"].values and listal[3] not in arquivo['Discussao'].values:
                    dfForum = arquivo
                    dfForum = dfForum.append(json,ignore_index=True)
                    gravaDados.persiste('forum', dfForum, nomeArq)
            else:
                dfForum = dfForum.append(json,ignore_index=True)
                gravaDados.persiste('forum', dfForum, nomeArq)
            
            
