str0 = "20M10000N80M"
expected_output = [('20', 'M'), ('10000', 'N'), ('80', 'M')]
assert test(str0) ==expected_output, 'Test failed'