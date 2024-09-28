var0 = pd.DataFrame({'A': ['lion', 'tiger', 'lion'], 'C': ['car', 'bus', 'car']})
expected_result =  pd.DataFrame({'A_lion': [1, 0, 1], 'A_tiger': [0, 1, 0], 'C_bus': [0, 1, 0], 'C_car': [1, 0, 1]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'