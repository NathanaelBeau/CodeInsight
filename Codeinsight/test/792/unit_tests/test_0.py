str0 = "aaabcabccd"
expected_result =  ['a', 'b', 'c', 'd']
assert sorted(test(str0)) == expected_result, 'Test failed'