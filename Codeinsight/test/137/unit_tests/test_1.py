var0 = 'country'
df0 = pd.DataFrame({'country': ['USA', None, 'CANADA', 'UK']})
expected_result =  pd.DataFrame({'country': ['usa', None, 'canada', 'uk']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'