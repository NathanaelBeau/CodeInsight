df0 = pd.DataFrame({ 'farm': ['A', 'B', 'C'], 'fruit': ['apple', 'banana', 'cherry'], '2019': [10, 20, 30], '2020': [15, 25, 35] })
lst0 = ['farm', 'fruit']
var0 = 'year'
var1 = 'value'
expected_output = pd.DataFrame({ 'farm': ['A', 'B', 'C', 'A', 'B', 'C'], 'fruit': ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry'], 'year': ['2019', '2019', '2019', '2020', '2020', '2020'], 'value': [10, 20, 30, 15, 25, 35] })
assert test(df0, lst0, var0, var1) .equals(expected_output), 'Test failed'