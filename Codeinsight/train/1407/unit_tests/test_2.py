df3 = pd.DataFrame({'scores': [100, 200, 300]})
assert test(df3, 'scores', 50) == 3  # All values above 50