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

museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath,index_col="Date",parse_dates=True)
museum_data.tail()
sns.lineplot(data=museum_data)
plt.figure(figsize=(12,6))
plt.title("Monthly Visitors to Avila Adobe")

sns.lineplot(data=museum_data['Avila Adobe'])
plt.xlabel("Date")
