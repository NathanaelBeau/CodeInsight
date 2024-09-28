str0 = "animal-Dog, breed-Golden Retriever, age-3"
expected_output = {'animal': 'Dog', 'breed': 'Golden Retriever', 'age': '3'}
assert test(str0) ==expected_output, 'Test failed'