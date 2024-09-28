df0 = pd.DataFrame({ 'Country': ['USA', 'Canada', 'Mexico'], 'Population': [331, 38, 126] })
var0 = 'Country'
expected_output = { 'USA': [331], 'Canada': [38], 'Mexico': [126] }
assert test(df0, var0) ==expected_output, 'Test failed'