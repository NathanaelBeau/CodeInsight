arg = pd.DataFrame({'City': ['New York', 'Los Angeles', 'Chicago'], 'Population': [8398748, 3990456, 2705994]})
expected_output = {'City': {0: 'New York', 1: 'Los Angeles', 2: 'Chicago'}, 'Population': {0: 8398748, 1: 3990456, 2: 2705994}}
assert test(arg) == expected_output, 'Test failed'