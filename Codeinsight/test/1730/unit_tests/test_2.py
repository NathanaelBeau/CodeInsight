var0 = r'hello (\w+) world (\d+)'
str0 = 'hello openai world 3, hello python world 2'
expected_output = [('openai', '3'), ('python', '2')]
assert test(var0, str0) == expected_output, 'Test failed'