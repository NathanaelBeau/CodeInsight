s0 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s1 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
expected_result =  pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'a', 'b', 'c'])
assert test(s0, s1).equals(expected_result), 'Test failed'