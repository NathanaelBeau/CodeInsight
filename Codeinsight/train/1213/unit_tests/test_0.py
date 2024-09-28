var0= 'name'
df0 = pd.DataFrame({'name': ['John (Doe)', 'Jane (Smith)', 'Mike (Johnson)']})
expected_result =  pd.DataFrame({'name': ['John ', 'Jane ', 'Mike ']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'