# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'apple', 'cherry'], 'color': ['red', 'yellow', 'red', 'red']})
lst0 = ['fruit', 'color']
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana', 'cherry'], 'color': ['red', 'yellow', 'red']})
result = test(df0, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'