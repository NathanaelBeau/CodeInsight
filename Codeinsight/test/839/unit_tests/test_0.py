df0 = pd.DataFrame({
            'Full Name': ['John Doe', 'Jane Smith', 'Alice Johnson']
        })
expected = pd.DataFrame({
            'Full Name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
            'First Name': ['John', 'Jane', 'Alice'],
            'Last Name': ['Doe', 'Smith', 'Johnson']
        })
result = test(df0, 'Full Name', 'First Name', 'Last Name')
assert result.equals(expected), 'Test failed'