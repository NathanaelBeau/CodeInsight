var0 = pd.DataFrame({'A': [7, 8, 9]})
expected_result =  pd.DataFrame({'A': [7, 8, 9], 'B': [49, 64, 81], 'C': [343, 512, 729]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'