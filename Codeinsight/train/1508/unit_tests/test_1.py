var0 = "The price is nearly 5 dollars but not more than 10 dollars."
lst0 = ["nearly", "not more than"]
expected_result =  ["nearly 5", "not more than 10"]
assert test_revised(var0, lst0) == expected_result, 'Test failed'