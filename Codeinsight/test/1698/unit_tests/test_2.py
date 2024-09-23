data = { 'Country': ['USA', 'USA', 'Canada', 'Canada', 'Canada', 'Mexico'], 'Population': [330, 350, 38, 42, 40, 128] }
df0 = pd.DataFrame(data)
var0 = 'Country'
var1 = 'Population'
# Résultat attendu
expected_output = df0.loc[[3, 5, 1]]
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'