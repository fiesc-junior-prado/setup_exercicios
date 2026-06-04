import pandas as pd
import numpy as np

# Dicionário com os dados brutos exportados pelo sistema legado
dados_brutos = {
    'id_venda': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'produto': [
        'Filamento PLA ', ' Placa Arduino', 'mdf 3mm', 'Filamento ABS', 
        'Sensor de Temperatura', 'Filamento PLA ', 'MDF 3mm', 'Motor de Passo', 
        np.nan, 'placa arduino'
    ],
    'quantidade': [2, -1, 5, np.nan, 10, 3, 0, 4, 2, 1],
    'preco_unitario': [
        'R$ 89,90', 'R$ 75.00', 'R$ 15,50', 'R$ 79.90', 'R$ 12,00', 
        'R$ 89,90', np.nan, 'R$ 45.00', 'R$ 50,00', '75.00'
    ],
    'data_venda': [
        '10/05/2026', '11/05/2026', '11/05/2026', '12/05/2026', '12/05/2026', 
        '13/05/2026', '13/05/2026', '14/05/2026', '15/05/2026', '15/05/2026'
    ]
}

df_vendas = pd.DataFrame(dados_brutos)