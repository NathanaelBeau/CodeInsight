import re

def test(var0):
    alphas = re.findall(r'[A-Za-z]+', var0)
    nums = re.findall(r'\d+', var0)
    return alphas, nums

