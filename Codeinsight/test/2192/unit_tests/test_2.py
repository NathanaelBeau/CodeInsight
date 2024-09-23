df0 = pd.DataFrame({'col': ['dog', 'cat']})
str0 = 'animal_'
expected_result =  pd.DataFrame({'col': ['animal_dog', 'animal_cat']})
assert test(df0, 'col', str0).equals(expected_result), 'Test failed'