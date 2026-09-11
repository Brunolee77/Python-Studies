import pandas as pd
import numpy as np

df_gerentes= pd.read_excel("gerentes_lojas.xlsx")
df_vendas= pd.read_csv("vendas_tech.csv", low_memory=False)

print(df_gerentes)
print(df_vendas)

#posso importar o (from pathlib import Path) com a linha de codigo: pasta = Path(__file__).parent para o python trabalhar com os documentos dentro da propria pasta.


