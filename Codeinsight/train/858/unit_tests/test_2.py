ndarr0 = np.array(['apple', 'banana', 'apple', 'cherry', 'banana'])
item0 = 'apple'
expected_result =  2
result = test(ndarr0, item0)
assert result == expected_result, 'Test failed'