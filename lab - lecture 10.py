import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

df = pd.read_csv(url_to_csv)

# 1. Explore the data.  How many categories of flowers are there? What
#    are the mean and median values?  How would you find the mean values
#    per type of flower (you don't actually have to implement this - we
#    will cover it next week)

df.describe()

# 2. Using one line of code, multiply every value by 100

def multiply(x):
    return x*100
df2 = df.apply(multiply)

# 3. Subset the data so only virginica flowers remain

df3 = df[df['species'] == 'virginica']

# 4. Create a new column named "petal_area" which is equal to the length
#    times the width
petalarea = df['petal_width'] * df['petal_length']
df['petal_area'] = petalarea
