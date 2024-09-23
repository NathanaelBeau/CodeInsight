var0 = "[This] is (a) test \"string\"."
expected_output = ['[This]', 'is', '(a)', 'test', '"string"', '.']
assert test(var0) == expected_output, 'Test failed'