lst0 = [
    {'Name': 'Alice', 'Age': 28},
    {'Name': 'Bob', 'Age': 32},
    {'Name': 'Claire', 'Age': 40}
]
expected_output = pd.DataFrame(lst0)
assert test(lst0) .equals(expected_output), 'Test failed'