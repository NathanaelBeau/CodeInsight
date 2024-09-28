var0 = "A B A B A B"
expected_result =  {("A", "B"): 3, ("B", "A"): 2}
assert test(var0) == expected_result, 'Test failed'