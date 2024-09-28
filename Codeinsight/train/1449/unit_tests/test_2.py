str0 = "python"
expected_result =  sorted(['p', 'y', 't', 'h', 'o', 'n'])
result = sorted(test(str0))
assert result==expected_result, 'Test failed'