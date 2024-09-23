df0 = pd.DataFrame({'col1': ['apple', 'banana', 'cherry', 'date'],
                    'col2': ['ant', 'bee', 'cat', 'dog']})
var0 = 'col2'
var1 = 't'
expected_output = [True, False, True, False]
assert test(df0, var0, var1) ==expected_output, 'Test failed'