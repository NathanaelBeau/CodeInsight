df = pd.DataFrame({ 'Name': ['Alice', 'Bob'], 'Age': [25, 30] })
expected_output = [
    {'Name': ['Alice', 'Bob']},
    {'Age': [25, 30]}
]
assert test(df) == expected_output, 'Test failed'