import pandas as pd

def test(df0, df1):
    combined_df = pd.concat([df0, df1], ignore_index=True)
    combined_df = combined_df.reset_index(drop=True)
    return combined_df
