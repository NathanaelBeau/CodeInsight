df0 = pd.DataFrame({ 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [28, 35, 22] })
var0 = 'Name'
expected_output = { 'Alice': [28], 'Bob': [35], 'Charlie': [22] }
assert test(df0, var0) ==expected_output, 'Test failed'