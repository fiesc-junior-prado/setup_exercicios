import pandas as pd
import numpy as np

# DataFrame 1: Vendas do mês de Janeiro
df_jan = pd.DataFrame({
    'ID_Cliente': [101, 102, 103, 104],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Qtd': [1, 3, 2, 1],
    'Preco_Unit': [4500, 120, 250, 1100]
})

# DataFrame 2: Vendas do mês de Fevereiro
df_fev = pd.DataFrame({
    'ID_Cliente': [102, 105, 106],
    'Produto': ['Monitor', 'Headset', 'Notebook'],
    'Qtd': [1, 2, 1],
    'Preco_Unit': [1100, 350, 4800]
})

# DataFrame 3: Cadastro Geral de Clientes
df_cadastro = pd.DataFrame({
    'ID_Cliente': [101, 102, 103, 105, 106, 107],
    'Nome_Cliente': ['ana silva', 'BRUNO COSTA', 'Carlos Souza', 'daniela lima', 'EDUARDO REIS', 'Fernanda Alves'],
    'Estado': ['SP', 'RJ', 'MG', 'SP', 'BA', 'PR']
})