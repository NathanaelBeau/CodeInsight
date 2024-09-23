from sklearn.preprocessing import StandardScaler

def test(arr0):
    scaler = StandardScaler()
    arr0 = scaler.fit_transform(arr0)
    return arr0