str0 = "split_by_indices"
lst0 = [5, 8]
expected_result =  ["split", "_by", "_indices"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'