df1 = pd.DataFrame({'scores': [10, 20, 30, 40, 50]})
assert test(df1, 'scores', 25) == 3  # 30, 40, 50 are above 25