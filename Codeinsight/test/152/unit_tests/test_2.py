var0 = pd.DataFrame({'A': [9, 10], 'B': [11, 12]})
expected_result3 = pd.DataFrame({'A': [0.45, 0.45454545454545453], 'B': [0.55, 0.5454545454545454]})
result3 = test(var0)
assert result3.equals(expected_result3), 'Test failed'