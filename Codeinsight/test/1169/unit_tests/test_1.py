lst0 = [{'apple': 10}, {'apple': 5, 'banana': 5}, {'banana': 3}]
expected_result =  {'apple': 15, 'banana': 8}
assert test(lst0) == expected_result, 'Test failed'