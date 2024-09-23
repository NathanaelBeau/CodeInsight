lst0 = [
    {'City': 'Paris', 'Population': 2200000},
    {'City': 'London', 'Population': 8900000},
    {'City': 'New York', 'Population': 8600000}
]
expected_output = pd.DataFrame(lst0)
assert test(lst0) .equals(expected_output), 'Test failed'