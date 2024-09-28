str0 = "('a', 'b', 'c')"
tpl0 = ('d', 'e', 'f')
expected_result =  ('d', 'e', 'f', 'a', 'b', 'c')
result = test(str0, tpl0)
assert result == expected_result, 'Test failed'