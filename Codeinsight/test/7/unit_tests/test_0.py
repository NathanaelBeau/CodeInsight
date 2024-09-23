str0 = "This is a test string with z's"
expected_output = ['Thi', ' i', ' a te', 't ', 'tring with ', "'", '']
assert test(str0) ==expected_output, 'Test failed'