lst0 = ['Python', 'java', 'JAVA', 'Python', 'C++']
expected_result =  ['c++', 'java', 'python']
result = test(lst0)
assert result == expected_result, 'Test failed'