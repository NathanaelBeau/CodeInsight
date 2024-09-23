df0 = pd.DataFrame({'Text': ['Hello', 'WORLD', None]})
expected = pd.DataFrame({'Text': ['hello', 'world', '']})
result = test(df0, 'Text')
assert result.equals(expected), 'Test failed'