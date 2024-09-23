arg = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
expected_output = {'Name': {0: 'Alice', 1: 'Bob', 2: 'Charlie'}, 'Age': {0: 25, 1: 30, 2: 35}}
assert test(arg) == expected_output, 'Test failed'