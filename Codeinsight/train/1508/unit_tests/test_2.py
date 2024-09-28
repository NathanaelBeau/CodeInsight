var0 = "I need at least 5 pens and at most 10 pencils."
lst0 = ["at least", "at most"]
expected_result =  ["at least 5", "at most 10"]
assert test_revised(var0, lst0) == expected_result, 'Test failed'