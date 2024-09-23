from sklearn.model_selection import train_test_split

def test(data0, train_size0, val_size0):
    train, intermediate = train_test_split(data0, test_size=1-train_size0)
    test_size0 = 1 - val_size0 / (1 - train_size0)
    val, test = train_test_split(intermediate, test_size=test_size0)
    return train, val, test
