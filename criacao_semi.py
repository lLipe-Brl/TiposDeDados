# SEMI ESTRUTURADO
# JSON

import pandas as pd

dados_json= {
    "Nome" : ["Benedito", "Gustavo", "Felicia", "Andre", "Julio", "Amanda"],
    "Idade" : [19, 18, 27, 30, 12, 50],
    "Cidade" : ["Curitiba", "Sao Paulo", "Rio de Janeiro", "Mato Grosso", "Ceara", "Sorocaba City"]
}

#CRIAR DATAFRAME (LINHAS E COLUNAS)
df_json = pd.DataFrame(dados_json)

# SALVAR EM JSON

df_json.to_json("dadosSemi.json", orient="records", lines=False)  





