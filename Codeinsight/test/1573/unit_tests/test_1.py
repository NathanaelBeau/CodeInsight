import pandas as pd
# Créer un DataFrame pour l'exemple de test
data = {'fruit': ['Apple', 'Banana', 'Cherry'], 'price': [0.99, 0.25, 1.50]}
df0 = pd.DataFrame(data)
df0.set_index('fruit', inplace=True)
expected_output = ['Apple', 'Banana', 'Cherry']
assert test(df0) == expected_output, 'Test failed'