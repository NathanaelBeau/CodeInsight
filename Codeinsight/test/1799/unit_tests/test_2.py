# Test 3
df0 = pd.DataFrame({'Col1': ['a', 'b', 'c'], 'Col2': ['d', 'e', 'f']})
df1 = pd.DataFrame({'Col1': ['a', 'b'], 'Col2': ['d', 'e']})
expected_result =  pd.DataFrame({'Col1': ['c'], 'Col2': ['f']}, index=[2])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'