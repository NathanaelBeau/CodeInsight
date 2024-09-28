class ModelObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def to_dict(self):
        return self.__dict__
lst0 = [ModelObject(name='John', age=25), ModelObject(name='Jane', age=30), ModelObject(name='Doe', age=35)]
expected_result =  pd.DataFrame([{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 35}])
result = test(lst0)
assert result.equals(expected_result), 'Test failed'