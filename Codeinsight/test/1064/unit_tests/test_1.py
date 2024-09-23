# Test 3
import os
current_directory = os.getcwd()
df0 = pd.DataFrame({"x": [10, 30, 50], "y": [20, 40, 60]})
filename = current_directory+"/test3.csv"
result = test(df0, filename)