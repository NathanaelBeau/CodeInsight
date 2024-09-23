dates = pd.date_range('20230101', periods=3)
df = pd.DataFrame({
            'A': [10, 20, 30],
            'B': [5, 15, 25]
        }, index=dates)
result = test(df)
expected = pd.DatetimeIndex(dates)
assert result .equals(expected), 'Test failed'