var0 = pd.DataFrame({ 'OldHeader1': ['NewHeader1', 'Value1', 'Value2'], 'OldHeader2': ['NewHeader2', 'Value3', 'Value4'] })
expected_result =  pd.DataFrame({ 'NewHeader1': ['Value1', 'Value2'], 'NewHeader2': ['Value3', 'Value4'] }, index=[1, 2])
result = test(var0)
assert result.equals(expected_result), 'Test failed'