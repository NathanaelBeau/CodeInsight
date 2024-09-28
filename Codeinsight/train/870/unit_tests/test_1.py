df0 = pd.DataFrame({"X": ["apple", "banana"], "Y": ["fruit", "fruit"]})
expected_result =  pd.Series(["apple fruit", "banana fruit"])
result = test(df0)
assert result.equals(expected_result), 'Test failed'