import pandas as pd
df0 = pd.DataFrame({ 'P': [1.5, 2.5, 3.5], 'Q': [4.5, 5.5, 6.5], 'R': [7.5, 8.5, 9.5] })
print(test(df0).equals(pd.DataFrame({
    'P': [-3.0, -3.0, -3.0],
    'Q': [0.0, 0.0, 0.0],
    'R': [3.0, 3.0, 3.0]
})))