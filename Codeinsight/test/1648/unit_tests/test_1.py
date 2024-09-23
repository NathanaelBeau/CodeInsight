datetime_obj = datetime.datetime(2024, 9, 23)
result = test(datetime_obj)
expected = pd.Timestamp(datetime_obj)
assert result == expected, f"Test Failed"