import pandas as pd
# Créer un DataFrame pour l'exemple de test
data = {'city': ['New York', 'San Francisco', 'Los Angeles'], 'population': [8398748, 883305, 3979576]}
df0 = pd.DataFrame(data)
df0.set_index('city', inplace=True)
expected_output = ['New York', 'San Francisco', 'Los Angeles']
assert test(df0) == expected_output, 'Test failed'