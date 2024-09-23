df0_test3 = pd.DataFrame({"C": ["hello", "world", "hello world", "world hello"]})
var0 = "C"
var1 = r"^hello world$"  # Strings exactly matching 'hello world'
expected_result =  pd.DataFrame({"C": ["hello", "world", "world hello"]})
assert test(df0_test3, var0, var1).equals(expected_result), 'Test failed'