str0 = "2010-11-13 10:33:54.227806"
expected_output = datetime(2010, 11, 13, 10, 33, 54, 227806)
assert test(str0) ==expected_output, 'Test failed'