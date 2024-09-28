df0 = pd.DataFrame({'a': ['apple', 'banana', 'cherry'], 'b': ['dog', 'elephant', 'fox'], 'c': ['giraffe', 'hippo', 'iguana']})
expected_result =  pd.Series(['dog', 'elephant', 'fox'], name='b')
result = test(df0)
assert result.equals(expected_result), 'Test failed'