import pandas
df1 = pandas.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pandas.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
expected_output = pandas.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
# Act
assert expected_output.equals(test(df1,df2)), 'Test failed'