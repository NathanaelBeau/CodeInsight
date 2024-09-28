lst0 = np.array([-1, -2, -3])
lst1 = np.array([-4, -5, -6])
expected_result =  np.sqrt((-1+4)**2 + (-2+5)**2 + (-3+6)**2)
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'