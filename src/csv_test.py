import pandas as pd

df = pd.read_csv('./exemplo.csv', sep=';')

df_filtrado = df[df['estado'] == 'SP']

print(df_filtrado)