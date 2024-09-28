lst0 = ["Hello\tWorld", "Python\tRocks", "GPT-4\tIs Cool"]
expected_result =  ["Hello", "Python", "GPT-4"]
result = test(lst0)
assert result == expected_result, 'Test failed'