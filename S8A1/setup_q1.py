import pandas as pd
import numpy as np

# Configuração para reprodutibilidade
np.random.seed(42)

# 1. DataFrame: Evolução Mensal (Vendas e Lucro)
dados_mensais = {
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Faturamento': [45000, 48000, 52000, 49000, 58000, 62000, 60000, 65000, 70000, 78000, 95000, 120000],
    'Lucro_Liquido': [9000, 10000, 11500, 9800, 13000, 14200, 13500, 15000, 17500, 20000, 26000, 35000]
}
df_mensal = pd.DataFrame(dados_mensais)

# 2. DataFrame: Desempenho por Categoria de Produto
dados_categorias = {
    'Categoria': ['Eletrônicos', 'Eletrodomésticos', 'Moda', 'Livros', 'Beleza'],
    'Unidades_Verdidas': [1250, 850, 2300, 1700, 1900]
}
df_categorias = pd.DataFrame(dados_categorias)

# 3. DataFrame: Impacto do Marketing Digital (30 dias de campanha)
investimento = np.random.uniform(500, 3500, 30)
retorno_clientes = 100 + (investimento * 0.12) + np.random.normal(0, 40, 30)

df_marketing = pd.DataFrame({
    'Investimento_Marketing': investimento,
    'Novos_Clientes': retorno_clientes
})