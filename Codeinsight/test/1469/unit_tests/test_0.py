var0 = 'one,"two,three",four,five,"six,seven",eight'
expected_result =  ['one', 'two,three', 'four', 'five', 'six,seven', 'eight']
result = test(var0)
assert result == expected_result, 'Test failed'