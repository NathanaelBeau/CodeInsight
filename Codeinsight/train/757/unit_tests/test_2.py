var0 = "No [brackets] or (parentheses) \"here\"."
expected_output = ['No', '[brackets]', 'or', '(parentheses)', '"here"', '.']
assert test(var0) == expected_output, 'Test failed'