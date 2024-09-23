import pandas as pd

def test(df0, str0, str1):
	return df0.loc[df0[str0] == str1]

