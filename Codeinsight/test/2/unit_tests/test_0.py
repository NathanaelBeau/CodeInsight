from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.datasets import load_iris
# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
# Train a decision tree classifier
clf = DecisionTreeClassifier(max_depth=2)  # Limiting depth for simplicity
clf.fit(X, y)
result = test(clf, feature_names)
expected_result =  export_text(clf, feature_names=feature_names)
assert result == expected_result, 'Test failed'