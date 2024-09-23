df0 = pd.DataFrame({"B": [4, 5, 6]}, index=["cat", "dog", "rat"])
arg0 = "at"
expected_output = pd.DataFrame({"B": [4, 6]}, index=["cat", "rat"])
assert test(df0, arg0).equals(expected_output), 'Test failed'