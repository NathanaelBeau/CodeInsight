class ModelObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def to_dict(self):
        return self.__dict__
lst0 = [ModelObject(x=10, y=20, z=30)]
expected_result =  pd.DataFrame([{'x': 10, 'y': 20, 'z': 30}])
result = test(lst0)
assert result.equals(expected_result), 'Test failed'