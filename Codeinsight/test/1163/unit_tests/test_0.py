lst0 = ['good', 'bad', 'tall', 'big']
lst1 = ['boy', 'girl', 'guy', 'man']
expected_output = ['goodboy', 'badgirl', 'tallguy', 'bigman']
assert test(lst0, lst1) ==expected_output, 'Test failed'