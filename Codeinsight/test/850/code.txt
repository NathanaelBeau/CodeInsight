import pandas as pd

def test(df0, frac0=0.75, random_state0=None):
    train = df0.sample(frac=frac0, random_state=random_state0)
    test = df0.drop(train.index)
    return train, test
