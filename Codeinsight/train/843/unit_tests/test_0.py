df0 = pd.DataFrame({'col': ['a,b', 'c,d', 'e,f']})
expected_result =  pd.DataFrame({0: ['a', 'c', 'e'], 1: ['b', 'd', 'f']})
result = test(df0, 'col')
assert result.equals(expected_result), 'Test failed'