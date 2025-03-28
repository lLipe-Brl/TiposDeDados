# DADOS ESTRUTURADOS - CRIAÇÃO
# EXCEL
# Terminal > pip install pandas > enter para instalar
# pip install openpyxl

import pandas as pd

#ESTRUTURA DE DICIONÁRIO
dados_planilha1 = {
    "Nome" : ["Benedito", "Gustavo", "Felícia", "André", "Julio", "Amanda"],
    "Idade" : [19, 18, 27, 30, 12, 50],
    "Cidade" : ["Curitiba", "São Paulo", "Rio de Janeiro", "Mato Grosso", "Ceará", "Sorocaba City"]
}

# CRIA UM DATAFRAME (LINHAS E COLUNAS)
df_planilha = pd.DataFrame(dados_planilha1)

# SALVAR NO EXCEL
with pd.ExcelWriter("dadosEstruturados.xlsx") as writer:
    df_planilha.to_excel(writer, sheet_name="Planilha1", index=False)

