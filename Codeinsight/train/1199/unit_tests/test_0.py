version = test()
pattern = r'^\d+\.\d+\.\d+$'
expected_result =  True
result = bool(re.match(pattern, version))
assert result == expected_result, 'Test failed'