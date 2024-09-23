def third_equations(vars):
    x, y = vars
    eq1 = x**3 - y**2 + 1
    eq2 = y**3 - x + 2
    return [eq1, eq2]
initial_guess = (1, -1)
expected_result =  fsolve(third_equations, initial_guess)
result = test(third_equations, initial_guess)
assert np.allclose(result, expected_result), 'Test failed'