df0 = pd.DataFrame({'Category': ['Fruit', 'Vegetable'], 'Quantity': [10, 5]})
expected_output = [{'Category': 'Fruit', 'Quantity': 10}, {'Category': 'Vegetable', 'Quantity': 5}]
assert test(df0) ==expected_output, 'Test failed'