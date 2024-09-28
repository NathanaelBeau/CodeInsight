import pandas 
var0 = pandas.DataFrame()
var1 = pandas.DataFrame({'A': [1, 2, 3]})
expected_result =  pandas.DataFrame({'A': [1, 2, 3]})
assert expected_result.equals(test(var0,var1)), 'Test failed'