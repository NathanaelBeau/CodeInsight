df0 = pd.DataFrame({'column_a': ['apple', 'bee', 'cherry', 'date'],
                    'column_b': ['ant', 'bee', 'cat', 'dog']})
var0 = 'column_b'
var1 = 'e'
expected_output = [False, True, False, False]
assert test(df0, var0, var1) ==expected_output, 'Test failed'