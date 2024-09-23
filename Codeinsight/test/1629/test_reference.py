from sklearn.impute import SimpleImputer
import numpy as np

def test(df0):
    imputer = SimpleImputer(strategy='most_frequent')
    return imputer.fit_transform(df0)

