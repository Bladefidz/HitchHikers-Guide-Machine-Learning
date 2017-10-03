import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

# Read dataset
df = pd.read_csv('sat_gpa.csv')
df.columns = ['high_GPA', 'math_SAT', 'verb_SAT', 'comp_GPA', 'univ_GPA']
df.head()

# Data visualization
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")
sns.lmplot('high_GPA', 'univ_GPA', data=df)
plt.xlabel('High School GPA')
plt.ylabel('Overall University GPA')
plt.show()  # The scatter plot will show linear correlation between High School GPA and University GPA