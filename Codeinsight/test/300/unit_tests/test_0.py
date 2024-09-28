df0 = pd.DataFrame({"A": ["apple*", "banana@", "fruit#"]})
col_name = "A"
expected_result =  pd.DataFrame({"A": ["apple", "banana", "fruit"]})
assert test(df0, col_name).equals(expected_result), 'Test failed'