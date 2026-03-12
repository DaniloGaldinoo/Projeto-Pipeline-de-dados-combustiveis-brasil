from pathlib import Path
import pandas as pd
import mysql.connector

raiz_projeto = Path(__file__).parent.parent.parent
pasta_raw = raiz_projeto / "data" / "raw"
arquivo_csv = pasta_raw / "Preços semestrais - AUTOMOTIVOS_2025.02.csv"
df = pd.read_csv(arquivo_csv, sep=";")

mapeamento = {'Regiao - Sigla': 'regiao',
              'Estado - Sigla': 'estado',
              'Municipio': 'municipio',
              'Revenda': 'revenda',
              'CNPJ da Revenda': 'cnpj',
              'Produto': 'produto',
              'Data da Coleta':'data_coleta',
              'Valor de Venda':'valor_venda',
              'Valor de Compra':'valor_compra',
              'Bandeira':'bandeira'
              }
df.rename(columns=mapeamento ,
          inplace=True
          )

colunasremover = ['Nome da Rua',
                  'Numero Rua',
                  'Complemento',
                  'Bairro',
                  'Cep',
                  'Unidade de Medida'
                  ]
df.drop(columns=colunasremover ,
        inplace=True
        )

df['valor_venda'] = df['valor_venda'].str.replace(',','.', regex=False).astype(float)
df['data_coleta'] = pd.to_datetime(df['data_coleta'], dayfirst=True)
df['cnpj'] = df['cnpj'].astype(str)
df['valor_compra'] = pd.to_numeric(
    df['valor_compra'].astype(str).str.replace(',', '.', regex=False), errors='coerce')

print (df.dtypes)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="combustiveis_anp"
)

cursor = conexao.cursor()

sql = """
INSERT INTO preco_combustivel(
    regiao, 
    estado, 
    municipio, 
    revenda, 
    cnpj, 
    produto,
    data_coleta, 
    valor_venda, 
    valor_compra, 
    bandeira)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

df = df.astype(object).where(pd.notnull(df), None)

dados = list(df[['regiao',
                 'estado',
                 'municipio',
                 'revenda',
                 'cnpj',
                 'produto',
                 'data_coleta',
                 'valor_venda',
                 'valor_compra',
                 'bandeira']].itertuples(index=False, name=None))

cursor.executemany(sql, dados)

conexao.commit()
print('Dados inseridos com sucesso!')

cursor.close()
conexao.close()
