df0 = pd.DataFrame({'grades': [85, 90, 95, 100]})
str0 = 'grades'
lst0 = [80, 90, 100]
expected_result =  pd.cut(df0['grades'], lst0)
result = test(df0, str0, lst0)
assert result.equals(expected_result), 'Test failed'