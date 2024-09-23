# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'elephant', 'fox']})
var0 = 'A'
var1 = r'^a'
expected_result =  pd.DataFrame({'A': ['apple'], 'B': ['dog']})
assert test(df0, var0, var1).equals(expected_result), 'Test failed'