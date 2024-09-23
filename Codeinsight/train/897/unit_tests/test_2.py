var0 = 'e'
var1 = pd.Series(['elephant', 'tiger', 'zebra'])
expected_result =  pd.Series(['elephant', 'tiger', 'zebra'])
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'