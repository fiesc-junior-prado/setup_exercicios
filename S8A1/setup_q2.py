import pandas as pd
import numpy as np

# Configuração para reprodutibilidade
np.random.seed(101)

# 1. DataFrame: Emissões de CO2 Mensais (Histórico do Ano)
dados_ambientais = {
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Emissoes_CO2_Toneladas': [120, 115, 110, 105, 98, 95, 99, 92, 88, 85, 80, 78]
}
df_emissoes = pd.DataFrame(dados_ambientais)

# 2. DataFrame: Consumo de Energia por Setor (Mês Atual)
dados_setores = {
    'Setor': ['Administração', 'Fundição', 'Montagem', 'Logística', 'Embalagem'],
    'Consumo_MWh': [45, 320, 180, 60, 95]
}
df_setores = pd.DataFrame(dados_setores)

# 3. DataFrame: Eficiência da Produção (Últimos 40 dias)
pecas_produzidas = np.random.randint(1000, 5000, 40)
energia_gasta = 200 + (pecas_produzidas * 0.15) + np.random.normal(0, 50, 40)

df_producao = pd.DataFrame({
    'Pecas_Produzidas': pecas_produzidas,
    'Energia_Consumida_kWh': energia_gasta
})