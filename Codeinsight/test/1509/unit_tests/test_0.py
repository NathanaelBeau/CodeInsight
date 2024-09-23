mylist = ['apple123', 'apple456', 'banana1', 'banana2', 'cherry', 'chocolate']
expected_output = [['apple123', 'apple456'], ['banana1', 'banana2'], ['cherry'], ['chocolate']]
assert test(mylist) == expected_output, 'Test failed'