df0 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [1, 2, 3]})
expected_output = pd.DataFrame({1: [2., 0., 0.],
                                 2: [0., 2., 0.],
                                 3: [0., 0., 2.],
                                 4: [1., 0., 0.],
                                 5: [0., 1., 0.],
                                 6: [0., 0., 1.],
},
                                index=df0.index)
assert test(df0).equals( expected_output), 'Test failed'