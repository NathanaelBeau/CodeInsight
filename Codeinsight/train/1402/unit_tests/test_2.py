df1 = pd.DataFrame({
        'fruits': ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    })
assert test(df1, 'fruits', 'apple') == 3 and test(df1, 'fruits', 'banana') == 2 and test(df1, 'fruits', 'orange') == 1, 'Failed test'