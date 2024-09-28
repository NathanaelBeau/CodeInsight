df0 = pd.DataFrame({ 'Column1': ['Apple', 'Banana', 'Cherry'], })
expected_result =  pd.Series(['Apple', 'Banana', 'Cherry'], name='Column1')
result = test(df0)
assert result.equals(expected_result), 'Test failed'