def test(df0):
    males = df0.query("Gender == 'Male' and Year == 2014")
    return males

