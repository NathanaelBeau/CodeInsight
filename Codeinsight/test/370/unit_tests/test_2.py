df0 = pd.DataFrame({"num1": ["1", "2"], "num2": ["3", "4"], "num3": ["5", "6"]})
expected_result =  pd.Series(["1 3 5", "2 4 6"])
result = test(df0)
assert result.equals(expected_result), 'Test failed'