str0 = "Mix"
lst0 = ["Apple", "5", "Banana"]
expected_result =  ["MixApple", "Mix5", "MixBanana"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'