df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Country': ['USA', 'UK', 'Canada']})
expected_output = [['Name', 'Alice', 'Bob', 'Charlie'], ['Age', 25, 30, 35], ['Country', 'USA', 'UK', 'Canada']]
assert test(df0)== expected_output, 'Test failed'