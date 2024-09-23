str0 = "No\u200bthing to \u200bre\u200bpl\u200bace here."
expected_output = "No*thing to *re*pl*ace here."
assert test(str0) ==expected_output, 'Test failed'