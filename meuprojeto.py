import pandas as pd

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(faturamento)

# quantidade de produtos vendidos por loja
quantidade_produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(quantidade_produtos)

#ticket médio
ticket_medio = (faturamento['Valor Final'] / quantidade_produtos['Quantidade']).to_frame()

print(ticket_medio)

