def test(var1):
    a=[]
    for i in range(2,var1+1):
        if(var1%i==0):
            a.append(i)
    a.sort()
    return a[0]