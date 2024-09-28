df0 = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60], "c": [70, 80, 90]})
result = test(df0)
expected_output = [(10, [70]), (20, [80]), (30, [90])]
assert result == expected_output, 'Test failed'