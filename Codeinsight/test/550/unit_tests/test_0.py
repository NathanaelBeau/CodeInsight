class ModelObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def to_dict(self):
        return self.__dict__
lst0 = [ModelObject(a=1, b=2), ModelObject(a=3, b=4)]
expected_result =  pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
result = test(lst0)
assert result.equals(expected_result), 'Test failed'