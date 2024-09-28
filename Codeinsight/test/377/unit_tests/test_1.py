df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date', 'applepie'], 'B': ['fruit', 'fruit', 'fruit', 'fruit', 'dessert']})
col0 = 'B'
str0 = 'fruit'
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date'], 'B': ['fruit', 'fruit', 'fruit', 'fruit']})
result = test(df0, col0, str0)
assert result.equals(expected_result), 'Test failed'