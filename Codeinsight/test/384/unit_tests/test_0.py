# Test 1
df0 = pd.DataFrame({'A': [10, 20], 'B': [30, 40], 'C': [50, 60]})
var0 = '^A|B$'
var1 = 2
expected_result =  pd.DataFrame({'A': [5.0, 10.0], 'B': [15.0, 20.0], 'C': [50, 60]})
assert test(df0, var0, var1).equals(expected_result), 'Test failed'