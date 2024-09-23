var0 = "I love python. python is great!"
replacements = {"python": "Python", "great": "awesome"}
expected_result =  "I love Python. Python is awesome!"
result = test(var0, replacements)
assert result == expected_result, 'Test failed'