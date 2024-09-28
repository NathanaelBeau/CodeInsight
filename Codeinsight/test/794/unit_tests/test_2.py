df0 = pd.DataFrame({ 'country': ['USA', 'Canada', 'Mexico'], 'population_2020': [331, 38, 129], 'population_2021': [334, 39, 130] })
lst0 = ['country']
var0 = 'year'
var1 = 'population'
expected_output = pd.DataFrame({ 'country': ['USA', 'Canada', 'Mexico', 'USA', 'Canada', 'Mexico'], 'year': ['population_2020', 'population_2020', 'population_2020', 'population_2021', 'population_2021', 'population_2021'], 'population': [331, 38, 129, 334, 39, 130] })
assert test(df0, lst0, var0, var1) .equals(expected_output), 'Test failed'