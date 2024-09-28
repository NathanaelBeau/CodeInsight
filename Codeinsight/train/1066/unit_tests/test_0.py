datetime_list = ["2024-09-23", "2024-09-24"]
result = test(datetime_list)
expected = pd.to_datetime(["2024-09-23", "2024-09-24"])
if pd.testing.assert_index_equal(pd.Index(result), pd.Index(expected)) is not None:
    assert False, 'Test failed'