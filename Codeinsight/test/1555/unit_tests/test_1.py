my_dict = { 'X': ['apple', 'banana', 'cherry'], 'Y': ['date', 'fig', 'grape'], 'Z': ['kiwi', 'mango', 'orange'] }
lst = ['banana', 'kiwi', 'lemon']
expected_output = ['X', 'Z']
assert test(my_dict, lst) == expected_output, 'Test failed'