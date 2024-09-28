var0 = pd.DataFrame({'C': ['a', 'b', 'c']}, index=pd.Index(['x', 'y', 'z'], name='index_name'))
expected_result =  pd.DataFrame({'C': ['a', 'b', 'c']}, index=pd.Index(['x', 'y', 'z']))
result = test(var0)
assert result.equals(expected_result), 'Test failed'