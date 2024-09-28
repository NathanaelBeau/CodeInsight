df0 = pd.DataFrame({'Event': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
                           'Status': ['Success', 'Success', 'Success', 'Failure', 'Success', 'Success', 'Failure']})
var0='Event'
var1='Status'
expected_output = pd.DataFrame({'Failure': [0, 1, 1], 'Success': [2, 1, 2]}, index=['A', 'B', 'C'])
result = test(df0, var0, var1)  
sorted_result = result[expected_output.columns]  # Réorganiser les colonnes pour correspondre à l'output attendu
sorted_result = sorted_result.reset_index(drop=True)
expected_output_reset = expected_output.reset_index(drop=True)
assert sorted_result.to_dict() == expected_output_reset.to_dict(), 'Test failed'