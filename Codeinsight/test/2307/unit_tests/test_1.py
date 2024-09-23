# Test 3
from sklearn.datasets import load_breast_cancer
dataset0 = load_breast_cancer()
df = test(dataset0)
assert df.shape == (569, 30), 'Test failed'