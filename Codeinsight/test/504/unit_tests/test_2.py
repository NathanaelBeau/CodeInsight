df0 = pd.DataFrame({ 'P': [100, 200, 300], 'Q': [400, 500, 600], 'Q_1': [700, 800, 900] })
expected_result =  pd.DataFrame({ 'P': [100, 200, 300], 'Q': [550, 650, 750] })
assert test(df0).equals(expected_result), 'Test failed'