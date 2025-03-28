# DADOS NÃO ESTRUTURADO - CRIAÇÃO
# CSV

import pandas as pd

dados_csv= {
    "Nome" : ["Benedito", "Gustavo", "Felicia", "Andre", "Julio", "Amanda"],
    "Idade" : [19, 18, 27, 30, 12, 50],
    "Cidade" : ["Curitiba", "Sao Paulo", "Rio de Janeiro", "Mato Grosso", "Ceara", "Sorocaba City"]
}


# CRIAR O DATAFRAME (LINHAS E COLUNAS)
df_csv = pd.DataFrame(dados_csv)

#SALVAR EM CSV
df_csv.to_csv("dadosNao.csv", index=False)
