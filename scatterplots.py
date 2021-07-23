import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/candy.csv"):
    os.symlink("../input/data-for-datavis/candy.csv", "../input/candy.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex4 import *
candy_filepath = "../input/candy.csv"


candy_data = pd.read_csv(candy_filepath,index_col="id")
print(candy_data.head())
sns.scatterplot(x=candy_data['sugarpercent'],y=candy_data['winpercent'])
sns.regplot(x=candy_data['sugarpercent'],y=candy_data['winpercent'])
sns.scatterplot(x=candy_data['sugarpercent'],y=candy_data['winpercent'],hue=candy_data['chocolate'])
sns.lmplot(x="pricepercent",y="winpercent",hue="chocolate", data=candy_data)
sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])
