from scipy.optimize import fsolve

def test(func, initial_guess):
    return fsolve(func, initial_guess)
