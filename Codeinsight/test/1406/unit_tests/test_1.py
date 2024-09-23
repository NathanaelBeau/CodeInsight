df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Priority': ['Medium', 'High', 'Low', 'Medium']
        })
priority_order = {'High': 1, 'Medium': 2}
result = test(df, 'Priority', priority_order)
expected = pd.DataFrame({
            'Name': ['Bob', 'Alice', 'David', 'Charlie'],
            'Priority': ['High', 'Medium', 'Medium', 'Low']
        }).reset_index(drop=True)
assert result.equals(expected), 'Test failed'