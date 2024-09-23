lst0 = ['Hello\tWorld', 'Python\tRocks', 'OpenAI\tGPT']
expected_result =  [['Hello', 'World'], ['Python', 'Rocks'], ['OpenAI', 'GPT']]
result = test(lst0)
assert result == expected_result, 'Test failed'