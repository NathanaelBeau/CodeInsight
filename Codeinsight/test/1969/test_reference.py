import pandas as pd

def test(var0):
	return pd.to_numeric(var0.stack(), 'coerce').unstack()