var0 = "A\n\nB\nC\nD"
expected_result =  [("A", "\nB\nC\nD")]
result = test(var0)
assert result == expected_result, 'Test failed'