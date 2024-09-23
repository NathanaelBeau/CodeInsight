import pandas as pd

def test(df0, df1):
    dataframeFinal = pd.merge(df0, df1, left_on=["room", "date", "hour"],
                    right_on=["room", "date", "hour"], how="outer",
                    left_index=False, right_index=False, copy=False)

    dataframeFinal["time_y"].fillna(dataframeFinal["time_x"], inplace=True)

    dataframeFinal = dataframeFinal.drop('time_x', axis=1)
    return dataframeFinal

