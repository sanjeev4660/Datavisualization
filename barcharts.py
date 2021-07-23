import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/ign_scores.csv"):
    os.symlink("../input/data-for-datavis/ign_scores.csv", "../input/ign_scores.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex3 import *
ign_filepath = "../input/ign_scores.csv"

ign_data = pd.read_csv(ign_filepath,index_col="Platform")
ign_filepath = "../input/ign_scores.csv"

ign_data =pd.read_csv(ign_filepath,index_col="Platform")
plt.figure(figsize=(8,6))
sns.barplot(x=ign_data['Racing'],y=ign_data.index)
plt.figure(figsize=(10,10))

sns.heatmap(data=ign_data, annot=True)
