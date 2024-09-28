df2 = pd.DataFrame({'scores': [5, 10, 15]})
assert test(df2, 'scores', 20) == 0  # No values above 20