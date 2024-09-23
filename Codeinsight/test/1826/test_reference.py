import pandas as pd
from sklearn.model_selection import train_test_split

def test(df0, frac0=0.75, random_state0=None):
    train, test = train_test_split(df0, train_size=frac0, random_state=random_state0)
    return train, test


