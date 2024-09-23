str0 = "fruit-Apple, color-Red, price-1.99"
expected_output = {'fruit': 'Apple', 'color': 'Red', 'price': '1.99'}
assert test(str0) ==expected_output, 'Test failed'