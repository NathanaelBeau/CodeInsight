df0 = pd.DataFrame({ 'X': ['apple', 'banana', 'apple', 'orange'], 'Y': ['orange', 'banana', 'banana', 'apple'], 'Z': ['grape', 'grape', 'grape', 'grape'] })
lst0 = ['X', 'Y']
expected_result =  (['apple', 'banana', 'orange'])
result = test(df0, lst0)
assert result == expected_result, 'Test failed'