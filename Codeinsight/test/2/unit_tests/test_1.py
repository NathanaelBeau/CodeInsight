from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.datasets import load_iris
# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
# Train a decision tree classifier
clf2 = DecisionTreeClassifier(max_depth=2)
clf2.fit(X[:, :2], y)  # Only first two features
result = test(clf2, feature_names[:2])
expected_result =  export_text(clf2, feature_names=feature_names[:2])
assert result == expected_result, 'Test failed'