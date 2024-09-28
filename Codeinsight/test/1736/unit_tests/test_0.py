df0 = pd.DataFrame({ 'prod_type': ['respon', 'r', 'other', 'respon'] })
var0 = 'prod_type'
dict0 = {'respon': 'responsive', 'r': 'responsive'}
    # Appeler la fonction que l'on teste
result_df = test(df0.copy(), var0, dict0)
    # Vérifier le résultat attendu
expected_output = pd.DataFrame({ 'prod_type': ['responsive', 'responsive', 'other', 'responsive'] })
assert test(df0, var0, dict0) .equals(expected_output), 'Test failed'