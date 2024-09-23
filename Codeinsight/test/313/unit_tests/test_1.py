# Test 2
df0 = pd.DataFrame({'X': ['cat', 'dog', 'bird']})
column_name = 'X'
prefix_string = 'animal_'
expected_result =  pd.DataFrame({'X': ['animal_cat', 'animal_dog', 'animal_bird']})
result = test(df0, column_name, prefix_string)
assert result.equals(expected_result), 'Test failed'