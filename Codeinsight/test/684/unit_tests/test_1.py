lst0 = [["apple", "banana", "cherry"], ["dog", "cat", "apple"], ["mouse", "keyboard", "banana"]]
expected_result =  [["dog", "cat", "apple"], ["mouse", "keyboard", "banana"], ["apple", "banana", "cherry"]]
result = test(lst0)
assert result == expected_result, 'Test failed'