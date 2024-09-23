df0 = pd.DataFrame({'A': ['hello', '[world]', '!'], 'B': ['[How]', 'are [you]', '[?]']})
expected_result =  pd.DataFrame({'A': ['hello', 'world', '!'], 'B': ['How', 'are you', '?']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'