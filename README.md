## Definição do Problema

A empresa entrou na bolsa de valores do Brasil há pouco tempo, com isso gostaríamos de saber como está sendo a precificação da nossa ação ao longo dos dias.

## Problema:
Dito isso, gostaríamos que você fizesse um algoritmo de web scrapping para que pudéssemos capturar essas informações.

Recomendamos o site abaixo, mas não precisa se ater a ele se não quiser.
https://br.advfn.com/bolsa-de-valores/bovespa/enjoei-com-br-atividades-on-ENJU3/cotacao

## Pontos de atenção:
1. Não se engane, o problema é simples, mas a ideia é ter algo que possa ser escalável e reutilizável.
Aplique conceitos de Orientação à Objeto e considere que esse fluxo irá rodar todos os dias (talvez toda hora), e não apenas uma vez.

2. Se preocupe com:
- documentação do código;
- documentação desse projeto;
- testes;
- tratamento de exceções;
- reutilização do código;
- reutilização do fluxo de dados.
    
3. Separe os dados de forma estruturada em arquivos e pastas via código.
- __dados:__
    - __balancos:__
    - __cotacoes:__
    - __forum:__
    - __noticias:__

4. Documente a tabela de forma a explicar que tipo de informações encontraremos nela.
- __dados:__ _pasta onde ficam armazenados todos os dados coletados._
    - __balancos:__ _pasta onde ficam armazenados os dados coletados do Balanço financeiro._
    - __cotacoes:__ _pasta onde ficam armazenados os dados coletados das cotações._
    - __forum:__ _pasta onde ficam armazenados os dados coletados do fórum de discução da empresa._
    - __noticias:__ _pasta onde ficam armazenados as noticias da empresa._

5. Escreva quais tipos de melhorias você faria na sua implementação.
- __Observação:__ O método dde scrapping só é aconcelhavel ser utilizado em caso de não termos outra forma de coleta, pois este pode parar de funcionar em caso de alteração da estrutura da pagina.
- __Melhorias:__ 
    - Contrataria a API da B3 e coletaria os dados da API
    - vincularia estas rotinas a uma nuvem, por Exempo GCP e faria as seguintes alterações:
        - Coletaria os dados e Colocaria na mesma estrutura de pastas em um Bucket do GCS
        - vincularia estes arquivos a uma tabela externa no BigQuery para vincular com um Software de DataViz

## Instalação e Execução ##
__Instalação__
- após clonar o repositório executar a linha abaixo no terminal dentro da pasta do projeto
    - pip install -r requirements.txt

__Execução__
- O projeto porde ser executado parcialmente colocando como parametro as rotinas que se deseja ou total retirando os parametros:
    - Executar com parametros: digite python main.py < acrecente os parametros > 
        - _cotacaes_: para recuperar os dados da cotação
        - _balancos_: para recuperar os dados do balanço financeiro
        - _balancos_: para recuperar os dados dos fóruns de discução
        - _balancos_: para recuperar os dados das notícias da empresa
    - Caso queira rodar todos digite apenas python main.py

