var0 = "one two one three one four"
expected_result =  {("one", "two"): 1, ("two", "one"): 1, ("one", "three"): 1, ("three", "one"): 1, ("one", "four"): 1}
assert test(var0) == expected_result, 'Test failed'