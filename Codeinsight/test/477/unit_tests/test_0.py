import pandas as pd
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9] })
print(test(df0).equals(pd.DataFrame({
    'A': [-3.0, -3.0, -3.0],
    'B': [0.0, 0.0, 0.0],
    'C': [3.0, 3.0, 3.0]
})))