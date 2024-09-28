str0 = 'Words, words, words.'
expected_result =  ['Words', ' words', ' words', '']
result = test(str0)
assert result == expected_result, 'Test failed'