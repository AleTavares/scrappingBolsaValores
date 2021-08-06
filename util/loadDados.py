import os

def persiste(pasta, dfDados, strNomeAqr):
    caminho = "./dados/{modulo}/{nomeArq}".format(modulo=pasta, nomeArq = strNomeAqr)
    if not os.path.exists('./dados'):
        os.mkdir('./dados')
    if not os.path.exists('./dados/'+pasta):
        os.mkdir('./dados/'+pasta)

    # Salvando o Arquivo em JSON 
    dfDados.to_json(caminho, orient="records")
