# coding: utf-8
import matplotlib as mpl
mpl.use('Agg')
import seaborn as sns

# this is an edit

df = sns.load_dataset('tips')
seaborn_plot = sns.pairplot(df)
seaborn_plot.savefig('pairplot.png')
