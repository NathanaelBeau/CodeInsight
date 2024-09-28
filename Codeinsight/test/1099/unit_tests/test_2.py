str0 = "\tTabs\t and\n new lines"
expected_result =  "Tabsandnewlines"
result = test(str0)
assert result == expected_result, 'Test failed'