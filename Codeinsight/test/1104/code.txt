from sklearn.model_selection import train_test_split
def test(X0, y0, var0, var1):
    return train_test_split(X0, y0, test_size=var0, random_state=var1)