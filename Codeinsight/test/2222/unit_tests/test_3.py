lst0 = [['apple',1], ['date',2], ['banana',2], ['cherry',5]]
expected_result =  [['apple',1], ['banana',2], ['cherry',5], ['date',2]]
result = test(lst0)
assert result == expected_result, 'Test failed'