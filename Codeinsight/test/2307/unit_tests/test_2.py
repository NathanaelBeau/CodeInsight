from sklearn.datasets import load_diabetes
dataset0 = load_diabetes()
df = test(dataset0)
assert df.shape == (442, 10), 'Test failed'