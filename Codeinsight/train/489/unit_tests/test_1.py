lst0 = ['python8', 'java8', 'c++8']
var0 = '8'
var1 = 'language'
expected_output = ['pythonlanguage', 'javalanguage', 'c++language']
assert test(lst0, var0, var1) == expected_output, 'Test failed'