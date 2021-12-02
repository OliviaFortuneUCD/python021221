import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

Ourdf = pd.read_csv('GBvideos.csv')

x=Ourdf['channel_title'].head(5)
y=Ourdf['likes'].head(5)
sns.lineplot(data=Ourdf, x=x, y=y)