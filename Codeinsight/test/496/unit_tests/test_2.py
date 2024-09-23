var0 = ['Name', 'Age', 'Score']
var1 = [
    np.array(['Alice', 'Bob', 'Charlie']),
    np.array([25, 30, 22]),
    np.array([85, 90, 78])
]
expected_output = pd.DataFrame({'Name': var1[0], 'Age': var1[1], 'Score': var1[2]})
assert test(var0, *var1) .equals(expected_output), 'Test failed'