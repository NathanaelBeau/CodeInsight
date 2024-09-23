df0 = pd.DataFrame({'Text': ['Hello', 'WORLD', 'Python']})
expected = pd.DataFrame({'Text': ['hello', 'world', 'python']})
result = test(df0, 'Text')
assert result.equals(expected), 'Test failed'