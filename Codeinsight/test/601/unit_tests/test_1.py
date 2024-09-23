input_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
expected_result =  ['red', 'blue', 'green', 'orange', 'yellow', 'indigo', 'violet']
result = test(input_list)
assert result==expected_result, 'Test failed'