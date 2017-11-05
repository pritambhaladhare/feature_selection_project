# Default imports
import pandas as pd
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap
from matplotlib import pyplot as plt
import seaborn as sns
data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = data.select_dtypes(include=numerics)
def plot_corr(df, size=11):
    plt.set_cmap('YlOrRd')
    plt.figure(figsize=(size,size))
    sns.heatmap(df.corr())
    plt.show()
