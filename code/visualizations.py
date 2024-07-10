# importing needed libraries
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import pandas as pd
import numpy as np

matplotlib_axes_logger.setLevel('ERROR')

# setting specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {
    'axes.titlesize': large,
    'legend.fontsize': med,
    'figure.figsize': (16, 10),
    'axes.labelsize': med,
    'xtick.labelsize': med,
    'ytick.labelsize': med,
    'figure.titlesize': large
}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

# creates a scatter plot with a trend line with the given data and parameters.
def scatter_plot_with_trend(data, x, y, title, xlabel, ylabel, save_path=None):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x, y=y)
    sns.regplot(data=data, x=x, y=y, scatter=False, color='red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()

# creates a bar plot with the given data and parameters.
def bar_plot(data, x, y, title, xlabel, ylabel, save_path=None):
    plt.figure(figsize=(14, 8))
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    
    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()
    
# creates a heatmap with the given data and parameters.
def heatmap(data, title, save_path=None):
    plt.figure(figsize=(12, 10))
    sns.heatmap(data, annot=True, cmap='coolwarm', center=0)
    plt.title(title)

    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()