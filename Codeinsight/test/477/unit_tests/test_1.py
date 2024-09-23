import pandas as pd
df0 = pd.DataFrame({ 'X': [10, 20, 30], 'Y': [40, 50, 60], 'Z': [70, 80, 90] })
print(test(df0).equals(pd.DataFrame({
    'X': [-30.0, -30.0, -30.0],
    'Y': [0.0, 0.0, 0.0],
    'Z': [30.0, 30.0, 30.0]
})))