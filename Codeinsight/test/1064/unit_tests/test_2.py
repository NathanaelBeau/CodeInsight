# Test 2
import os
current_directory = os.getcwd()
df0 = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
filename = current_directory  + "/test2.csv"
result = test(df0, filename)