dict0 = {'MixedCASE': 123, 'anotherOne': 456}
expected_result =  {'mixedcase': 123, 'anotherone': 456}
result = test(dict0)
assert result == expected_result, 'Test failed'