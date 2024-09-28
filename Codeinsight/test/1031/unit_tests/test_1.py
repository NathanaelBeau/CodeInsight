dict0= { 'New York City': 'NYC', 'San Francisco': 'SF', 'Los Angeles': 'LA', 'Chicago': 'CHI', 'Miami': 'MIA' }
arg0 = 'LOS'
expected_output = ['LA']
assert test(dict0, arg0) ==expected_output, 'Test failed'