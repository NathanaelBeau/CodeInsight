df = pd.DataFrame({ 'X': [10, 20], 'Y': [30, 40] })
expected_output = [
    {'X': [10, 20]},
    {'Y': [30, 40]}
]
assert test(df) == expected_output, 'Test failed'