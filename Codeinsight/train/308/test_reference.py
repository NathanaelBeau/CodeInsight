from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd 
def test(df0, col0):
    mlb = MultiLabelBinarizer()
    encoded = mlb.fit_transform(df0[col0])
    return pd.DataFrame(encoded, columns=mlb.classes_)
