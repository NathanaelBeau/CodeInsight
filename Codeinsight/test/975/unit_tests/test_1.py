def another_equations(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 5
    eq2 = x - y + 1
    return [eq1, eq2]
initial_guess = (2, 1)
expected_result =  fsolve(another_equations, initial_guess)
result = test(another_equations, initial_guess)
assert np.allclose(result, expected_result), 'Test failed'