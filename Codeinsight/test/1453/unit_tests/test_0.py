lst0 = ['Jellicle', 'Cats', 'are', 'black', 'and', 'white,', 'Jellicle', 'Cats', 'are', 'rather', 'small;', 'Jellicle', 'Cats', 'are', 'merry', 'and', 'bright,', 'And', 'pleasant', 'to', 'hear', 'when', 'they', 'caterwaul.', 'Jellicle', 'Cats', 'have', 'cheerful', 'faces,', 'Jellicle', 'Cats', 'have', 'bright', 'black', 'eyes;', 'They', 'like', 'to', 'practise', 'their', 'airs', 'and', 'graces', 'And', 'wait', 'for', 'the', 'Jellicle', 'Moon', 'to', 'rise.', '']
expected_output= ['Jellicle', 'Cats', 'are']
assert test(lst0)== expected_output, 'Test failed'