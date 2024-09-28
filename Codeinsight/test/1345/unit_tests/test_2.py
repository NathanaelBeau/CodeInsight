from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.datasets import load_iris
# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
# Train a decision tree classifier
clf3 = DecisionTreeClassifier(max_depth=2)
clf3.fit(X[y != 2], y[y != 2])  # Excluding one class
result = test(clf3, feature_names)
expected_result =  export_text(clf3, feature_names=feature_names)
assert result == expected_result, 'Test failed'