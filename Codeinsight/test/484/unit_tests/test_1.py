str0 = "OpenAI|GPT-3.5|model"
lst0 = ["|"]
expected_output = ["OpenAI", "GPT-3.5", "model"]
assert test(str0, lst0) ==expected_output, 'Test failed'