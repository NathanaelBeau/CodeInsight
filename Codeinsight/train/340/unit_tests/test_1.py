# Test 2
df0 = pd.DataFrame({'X': ['apple', 'banana'], 'Y': ['red', 'yellow']})
expected_result =  np.array([('apple', 'red'), ('banana', 'yellow')])
result = test(df0)
assert np.array_equal(result, expected_result), 'Test failed'