import pandas
df1 = pandas.DataFrame()
df2 = pandas.DataFrame()
expected_output = pandas.DataFrame()
# Act
assert expected_output.equals(test(df1,df2)), 'Test failed'