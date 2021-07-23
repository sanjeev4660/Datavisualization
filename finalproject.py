import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
my_filepath = "../input/ipl/deliveries.csv"
sns.barplot(x=my_data.index, y=my_data['batting_team'])
