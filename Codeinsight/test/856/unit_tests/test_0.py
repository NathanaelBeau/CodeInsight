df0 = pd.DataFrame({'AB': ['Hello World', 'Python Programming', 'Data Science']})
var0 = 'AB'
var1 = ['A', 'B']
expected_output = pd.DataFrame({'AB': ['Hello World', 'Python Programming', 'Data Science'],
                               'A': ['Hello', 'Python', 'Data'],
                               'B': ['World', 'Programming', 'Science']})
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'