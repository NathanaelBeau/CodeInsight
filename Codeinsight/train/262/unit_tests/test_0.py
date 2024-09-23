df0 = pd.DataFrame({"A": [1, 2, 3]}, index=["apple", "banana", "pineapple"])
arg0 = "apple"
expected_output = pd.DataFrame({"A": [1, 3]}, index=["apple", "pineapple"])
assert test(df0, arg0).equals(expected_output), 'Test failed'