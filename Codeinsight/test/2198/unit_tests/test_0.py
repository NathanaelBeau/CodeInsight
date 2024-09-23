# Unit Test 1
df0 = pd.DataFrame({ 'date': ['2023-01-01', '2023-01-01', '2023-01-02'], 'name': ['A', 'B', 'C'], 'dollars': [10, 20, 30] })
var0 = 'date'
var1 = 'name'
var2 = 'dollars'
expected_result =  pd.DataFrame({ 'A': [10.0, None], 'B': [20.0, None], 'C': [None, 30.0] }, index=['2023-01-01', '2023-01-02'])
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'