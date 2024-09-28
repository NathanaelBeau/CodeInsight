lst0 = [
    {'Name': 'John', 'Age': 25},
    {'Name': 'Emily', 'Age': 30},
    {'Name': 'Michael', 'Age': 35}
]
expected_output = pd.DataFrame(lst0)
assert test(lst0) .equals(expected_output), 'Test failed'