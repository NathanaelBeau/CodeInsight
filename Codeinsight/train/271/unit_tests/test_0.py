lst0 = [0, 0, 0, 0]
lst1 = [1, 1, 0, 1]
lst2 = [0, 0, 0, 1]
lst3 = [0, 1, 1, 0]
var0 = ['var1', 'var2', 'var3', 'var4']
expected_output = ['var2', 'var2, var4', 'var4', 'var2, var3']
assert test(lst0, lst1, lst2, lst3, var0) ==expected_output, 'Test failed'