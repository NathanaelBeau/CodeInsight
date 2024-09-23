def equations(vars):
    x, y = vars
    eq1 = x + y**2 - 4
    eq2 = x**2 + y - 2
    return [eq1, eq2]
initial_guess = (1, 1)
expected_result =  fsolve(equations, initial_guess)
result = test(equations, initial_guess)
assert np.allclose(result, expected_result), 'Test failed'