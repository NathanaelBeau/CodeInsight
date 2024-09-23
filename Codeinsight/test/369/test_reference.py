import pandas as pd

def test(dict0):
    df = pd.DataFrame(dict0.items(), columns=['Key', 'Value'])
    df['Average'] = df['Value'].apply(lambda x: sum(x) / len(x))
    averaged_tuples = list(zip(df['Key'], df['Average']))
    return averaged_tuples
