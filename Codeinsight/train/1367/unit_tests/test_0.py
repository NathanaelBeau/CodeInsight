lst0 = ["x (LOC)", "ds ds (32C)", "d'ds ds (LeC)", "ds-d da(LOQ)", "12345 (deC)"]
expected_output = ["x", "ds ds", "d'ds ds", "ds-d da(LOQ)", "12345"]
assert test(lst0) ==expected_output, 'Test failed'