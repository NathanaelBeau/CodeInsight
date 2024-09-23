df0 = pd.DataFrame({'a': ['apple', 'banana', 'cherry', 'date'],
                    'b': ['ant', 'bee', 'cat', 'dog']})
var0 = 'a'
var1 = 'a'
expected_output = [True, True, False, True]
assert test(df0, var0, var1) ==expected_output, 'Test failed'