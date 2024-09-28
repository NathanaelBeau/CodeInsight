dict0 = { "dog": "animal", "cat": "animal", "horse": "animal" }
var0 = "I have a DOG, a Cat, and a horse."
expected_output = "I have a animal, a animal, and a animal."
assert test(dict0, var0) ==expected_output, 'Test failed'