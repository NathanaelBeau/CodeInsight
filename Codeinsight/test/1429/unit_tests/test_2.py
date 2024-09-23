df0 = pd.DataFrame({ 'timestamp': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']), 'value': [2, 4, 6] })
str0 = 'timestamp'
var0 = '2D'  # Intervalle de temps de 2 jours
expected_result =  pd.DataFrame({ 'timestamp': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']), 'value': [2.0, 3.0, 5.0] })
result = test(df0, str0, var0).equals(expected_result)