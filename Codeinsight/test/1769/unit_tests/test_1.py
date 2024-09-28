df0 = pd.DataFrame({"B": ["dog", "cat", "rat", "bat", "mat"]})
var0 = "B"
var1 = r"at$"  # Strings ending with 'at'
expected_result =  pd.DataFrame({"B": ["dog"]})
assert test(df0, var0, var1).equals(expected_result), 'Test failed'