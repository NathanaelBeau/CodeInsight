lst0 = ["split me", "into words"]
expected_result =  [["split", "me"], ["into", "words"]]
result = test(lst0)
assert result == expected_result, 'Test failed'