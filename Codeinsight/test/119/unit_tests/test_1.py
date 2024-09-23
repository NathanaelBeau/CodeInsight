lst0 = ['@apple', '@banana', '@cherry', 'date']
char0 = '@'
expected_result =  ['date']
result = test(lst0, char0)
assert result == expected_result, 'Test failed'