df0 = pd.DataFrame({'Xtest': [10, 20, 30], 'Btest': [40, 50, 60], 'Xscore': [70, 80, 90]})
expected_result =  pd.DataFrame({'Xtest': [10, 20, 30], 'Xscore': [70, 80, 90]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'