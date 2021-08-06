import re
from unidecode import unidecode
import util.loadDados as gravaDados
from datetime import date
import os
import pandas as pd

def balanco(soup):

    # Pegando as linhas da tabela 
    info = soup.find_all(class_="TableElement")


    # Tratando os dados
    cont = 0
    lista = []
    for x in info:
        x = str(x)
        limpo = x.replace('</td>','|')
        clean = re.compile('<td.*?>')
        limpo = re.sub(clean, '|', limpo)
        clean = re.compile('<th.*?>.*?</th>')
        limpo = re.sub(clean, '', limpo)
        clean = re.compile('<.*?>')
        limpo = re.sub(clean, '', limpo)
        limpo = limpo.replace('\n', '').replace('\xa0','')
        limpo = unidecode(limpo)
        limpo = limpo.replace('[', '')
        limpo = limpo.replace(']', '')
        limpo = limpo.replace('||', '|')


        listLinhas = limpo.split('|')


        if cont > 7 and cont < 10:
            lista += listLinhas
        cont = cont + 1

        

    # Tranformando o dado em Json
    json = {
        'ValordeMercado':lista[1],
        'AcoesnaBolsadeValores':lista[2],
        'AcoesemCirculacao':lista[3],
        'Receita':lista[4],
        'Lucro/PrejuizodaEnjoeiS.A.':lista[5],
        'LucroporAcao(EPS)':lista[6],
        'PrecoporLucro(PE Ratio)':lista[7],
        'InteressedosVendidos':lista[10],
        'DividendosporAcao':lista[11],
        'RendimentodoDividendo':lista[12],
        'DataPrevistadoDividendo':lista[13],
        'InsiderC/V':lista[14],
        'PorcentagemdosControladores':lista[15]
    }

    # Data e Ano Atual
    data_atual = (date.today())
    
    dfbalancos = pd.DataFrame()

    # Salvando o Arquivo em JSON
    nomeArq = "balanco{data}.json".format(data = str(data_atual))
    caminho = "./dados/balancos/"+nomeArq

    if os.path.exists(caminho):
        dfbalancos = pd.read_json(caminho)
        if lista[0] not in dfbalancos["ValordeMercado"].values and lista[4] not in dfbalancos['Receita'].values:
            dfbalancos = dfbalancos.append(json,ignore_index=True)
    else:
        dfbalancos = dfbalancos.append(json,ignore_index=True)
    gravaDados.persiste('balancos', dfbalancos, nomeArq)