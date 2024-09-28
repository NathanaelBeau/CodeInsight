df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date', 'applepie'], 'B': ['fruit', 'fruit', 'fruit', 'fruit', 'dessert']})
col0 = 'A'
str0 = 'apple'
expected_result =  pd.DataFrame({'A': ['apple', 'applepie'], 'B': ['fruit', 'dessert']})
result = test(df0, col0, str0)
assert result.equals(expected_result), 'Test failed'