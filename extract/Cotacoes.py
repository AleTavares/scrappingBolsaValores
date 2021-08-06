# DESCRIÇÂO: Este módulo coleta dados de cotação

# Importação dos modulos necessarios para a coleta dos dados
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from unidecode import unidecode
from datetime import date
import os
import util.loadDados as gravaDados

def cotacao(soup):
    # Pegando as linhas da tabela de Cotações
    info = soup.find_all(class_="TableElement")

    # Limpeza dos dados
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
        
        if len(listLinhas) > 1 and cont < 6:
            lista += listLinhas
        cont = cont + 1

    # Data Atual
    data_atual = (date.today())

    # Cria variaveis de parametros pra salvar os dados
    anoMes = str(data_atual.year) + str(data_atual.month)
    nomeArq = 'cotacao'+anoMes+'.json'

    json = {
        "data_atual": str(data_atual),
        "NomedaAcao":lista[1],
        "CodigodaAcao":lista[2],
        "BolsadeValores":lista[3],
        "TipodeAtivo":lista[4],
        "VariacaodoDia(p)":lista[8],
        "VariacaodoDia%":lista[9],
        "UltimoPreco":lista[10],
        "Hora":lista[11],
        "PrecodeAbertura":lista[14],
        "PrecoMinimo":lista[15],
        "PrecoMaximo":lista[16],
        "FechHoje":lista[17],
        "FechAnterior":lista[18],
        "MelhorPrecodeCompra":lista[21],
        "MelhorPrecodeVenda":lista[22],
        "SpreaddePreco":lista[23],
        "NoticiasSobreENJU3":str(lista[24]) +'/'+ str(lista[25]),
        "NumerodeNegocios":lista[28],
        "VolumedeAcoesNegociadas":lista[29],
        "PrecoMedio":lista[30],
        "VolumeFinanceiro":lista[31],
        "Volumemedio":lista[32],
        "Ultimas52Semanas":lista[33],
        "UltimoNegocio":lista[36],
        "TipodeNegocio":lista[37],
        "QuantidadedeAcoesNegociadas":lista[38],
        "PrecoNegociado":lista[39],
        "Moeda":lista[40]
    }

    # Cria um data Frame em branco
    dfCotacao = pd.DataFrame()

    # Verifica e grava os dados
    if os.path.exists('./dados/cotacoes/'+nomeArq):
        arquivo = pd.read_json('./dados/cotacoes/'+nomeArq)
        if anoMes not in arquivo["data_atual"].values and lista[39] not in arquivo['Hora'].values:
            dfCotacao = arquivo
            dfCotacao = dfCotacao.append(json,ignore_index=True)
            gravaDados.persiste('cotacoes', dfCotacao, nomeArq)
    else:
        dfCotacao = dfCotacao.append(json,ignore_index=True)
        gravaDados.persiste('cotacoes', dfCotacao, nomeArq)
