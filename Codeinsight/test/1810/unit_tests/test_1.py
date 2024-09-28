# Test 2
df0 = pd.DataFrame({ 'banana': [10, 20, 30], 'apple': [40, 50, 60], 'cherry': [70, 80, 90] })
expected_result =  pd.DataFrame({ 'apple': [40, 50, 60], 'banana': [10, 20, 30], 'cherry': [70, 80, 90] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'