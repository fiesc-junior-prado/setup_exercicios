import pandas as pd
import numpy as np

# DataFrame 1: Histórico de visualizações (Semana 1)
df_sem1 = pd.DataFrame({
    'ID_Usuario': [1, 2, 3, 1],
    'Titulo': ['Matrix', 'Inception', 'O Poderoso Chefão', 'Shrek'],
    'Minutos_Assistidos': [120, 45, 180, 90]
})

# DataFrame 2: Histórico de visualizações (Semana 2)
df_sem2 = pd.DataFrame({
    'ID_Usuario': [2, 4, 3],
    'Titulo': ['Batman', 'Matrix', 'Interestelar'],
    'Minutos_Assistidos': [150, 30, 160]
})

# DataFrame 3: Cadastro de Usuários e Planos
df_usuarios = pd.DataFrame({
    'ID_Usuario': [1, 2, 3, 5],
    'Nome': ['Alice', 'Beto', 'Carla', 'Diego'],
    'Plano': ['basico', 'premium', 'premium', 'basico']
})