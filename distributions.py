import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/cancer_b.csv"):
    os.symlink("../input/data-for-datavis/cancer_b.csv", "../input/cancer_b.csv")
    os.symlink("../input/data-for-datavis/cancer_m.csv", "../input/cancer_m.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex5 import *
cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"

 cancer_b_data = pd.read_csv(cancer_b_filepath,index_col="Id")

 cancer_m_data = pd.read_csv(cancer_m_filepath,index_col="Id")
cancer_b_data.head()
print(cancer_m_data.head())
sns.distplot(a=cancer_b_data['Area (mean)'], kde=False) 
 sns.distplot(a=cancer_m_data['Area (mean)'], kde=False) 
sns.kdeplot(data=cancer_b_data['Radius (worst)'], shade=True)
 sns.kdeplot(data=cancer_m_data['Radius (worst)'], shade=True)
