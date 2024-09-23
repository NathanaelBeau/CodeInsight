# Test 1
import os
current_directory = os.getcwd()
df0 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
filename = current_directory+"/test1.csv"
result = test(df0, filename)