lst0 = ['abc/123', 'def/456', 'ghi/jkl', 'mno/789', 'pqr']
expected_output = ['123', '456', 'jkl', '789']
assert test(lst0) ==expected_output, 'Test failed'