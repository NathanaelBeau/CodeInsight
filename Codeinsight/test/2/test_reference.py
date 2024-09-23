from sklearn.tree import export_text
def test(tree0, feature_names0):
    return export_text(tree0, feature_names=feature_names0)

