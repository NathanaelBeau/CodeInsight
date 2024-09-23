def test(var1):
    sum_ = 0
    for i in range(1, var1//2 + 1):
        if var1%i == 0:
            sum_+=i
    if sum_ == var1:
        return True
    return False