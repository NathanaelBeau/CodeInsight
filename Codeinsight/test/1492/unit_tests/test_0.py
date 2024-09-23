df0 = pd.DataFrame({'stats': ["(1,2,3)", "(4,5,6)", "(7,8,9)"]})
# Nom de la colonne à traiter
var0 = 'stats'
# Sortie attendue après l'application de la fonction "test" sur le DataFrame avec la colonne spécifiée
expected_output = pd.DataFrame({'col1': [1.0, 4.0, 7.0],
                                'col2': [2.0, 5.0, 8.0],
                                'col3': [3.0, 6.0, 9.0]})
assert test(df0, var0).values.tolist() ==expected_output.values.tolist(), 'Test failed'