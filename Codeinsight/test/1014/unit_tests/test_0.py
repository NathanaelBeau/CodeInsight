dict0 = {"one": [(1,3),(1,4)], "two": [(1,2),(1,2),(1,3)], "three": [(1,1)]}
expected_output = ["two", "one", "three"]
assert test(dict0) ==expected_output, 'Test failed'