mylist = ['abcde1', 'abcde2', 'fghij', 'klmno', 'opqrs']
expected_output = [['abcde1', 'abcde2'], ['fghij'], ['klmno'], ['opqrs']]
assert test(mylist) == expected_output, 'Test failed'