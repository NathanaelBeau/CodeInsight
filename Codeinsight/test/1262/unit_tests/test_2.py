lst0 = [{'product': 'apple', 'prices': {'store1': 2, 'store2': 2.5}}, {'product': 'banana', 'prices': {'store1': 1, 'store2': 1.2}}]
expected_result =  pd.DataFrame({'product': ['apple', 'banana'], 'prices.store1': [2, 1], 'prices.store2': [2.5, 1.2]})
assert test(lst0).equals(expected_result), 'Test failed'