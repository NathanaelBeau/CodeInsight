lst2 = []
# Handle the edge case where the list is empty
try:
    test(lst2)
    print(False)  # This line shouldn't be reached
except IndexError:
    assert True, 'Test failed'