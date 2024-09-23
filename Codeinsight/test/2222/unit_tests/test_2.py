lst0 = [[1,'steve'],[4,'jane'],[3,'frank'],[2,'kim']]
expected_result =  [[1, 'steve'], [2, 'kim'], [3, 'frank'], [4, 'jane']]
result = test(lst0)
assert result == expected_result, 'Test failed'