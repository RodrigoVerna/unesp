# Universidade Estudual Paulista - Julio de Mesquista Filho (UNESP) - IBILCE
# Importador de arquivos excel v1.0
# Criado por: Rodrigo Perez Verna em 08/05/2024
# Contato: rodrigo.verna@unesp.br

import pandas as pd

# Carregar dados
alostericSites = pd.read_csv("unesp\data\AlostericSitesaa.csv", sep=',', on_bad_lines='skip', 
                                low_memory=False)

print(alostericSites.head(5))
