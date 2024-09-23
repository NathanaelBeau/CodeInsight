df = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9] })
expected_output = [
    {'A': [1, 2, 3]},
    {'B': [4, 5, 6]},
    {'C': [7, 8, 9]}
]
assert test(df) == expected_output, 'Test failed'