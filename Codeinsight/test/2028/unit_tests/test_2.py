# Test 2
df0 = pd.DataFrame({"B": [10, 20, 30]}, index=[10, 20, 30])
expected_result =  pd.DataFrame({"index": [10, 20, 30], "B": [10, 20, 30]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'