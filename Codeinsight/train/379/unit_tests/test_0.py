lst0 = ["Hello World", "Python Rocks"]
expected_result =  [["Hello", "World"], ["Python", "Rocks"]]
result = test(lst0)
assert result == expected_result, 'Test failed'