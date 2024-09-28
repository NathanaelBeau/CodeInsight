arr0 = np.array([[1,2,3],[4,5,6],[7,8,9]])
lst0 = ['row1', 'row2', 'row3']
lst1 = ['col1', 'col2', 'col3']
expected_result =  pd.DataFrame(arr0, index=lst0, columns=lst1)
result = test(arr0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'