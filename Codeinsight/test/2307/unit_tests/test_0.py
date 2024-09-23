from sklearn.datasets import load_iris
# Test 1
dataset0 = load_iris()
df = test(dataset0)
assert df.shape == (150, 4), 'Test failed'