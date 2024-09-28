df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
def mean_func(x):
    return x.mean()

result = test(df, mean_func, axis0=1)
expected = pd.Series([2.5, 3.5, 4.5], index=[0, 1, 2])
assert result.equals(expected), 'Test failed'