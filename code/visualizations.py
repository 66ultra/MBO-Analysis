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
plt.style.use('default')
sns.set_style("white")

# creates a scatter plot with a trend line with the given data and parameters.
def scatter_plot_with_trend_1(data, x, y, title, xlabel, ylabel, save_path=None):
    plt.figure(figsize=(10, 6))
    sns.regplot(data=data, x=x, y=y, scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'red'})
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()
    
# creates a scatter plot with a trend line with the given data and parameters.
def scatter_plot_with_trend_2(data, x, y, title, xlabel, ylabel, save_path=None):
    plt.figure(figsize=(10, 6))
    sns.regplot(data=data, x=x, y=y, scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'green'})
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()
    
# creates a scatter plot with a trend line with the given data and parameters.
def scatter_plot_with_trend_3(data, x, y, title, xlabel, ylabel, save_path=None):
    plt.figure(figsize=(10, 6))
    sns.regplot(data=data, x=x, y=y, scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'blue'})
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()
    
# creates a bar plot with the given data and parameters.
def bar_plot(data, column, value, threshold, title, xlabel, ylabel, save_path=None):
    # filtering out genres with less than a certain number of movies
    genre_counts = data[column].value_counts()
    popular_genres = genre_counts[genre_counts > threshold].index  # Adjust the threshold as needed
    filtered_data = data[data[column].isin(popular_genres)]

    # recalculating the average rating by genre
    avg_rating_by_genre = filtered_data.groupby(column)[value].mean().sort_values()

    # plotting the bar plot
    plt.figure(figsize=(12, 8))
    sns.barplot(
        x=avg_rating_by_genre.values,
        y=avg_rating_by_genre.index, 
        hue=avg_rating_by_genre.index, 
        palette='viridis', dodge=False
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend([],[], frameon=False)  # Hide the legend

    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()
    
# creates a heatmap with the given data and parameters.
def heatmap(data, title, save_path=None):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap='coolwarm', vmin=0, vmax=1)
    plt.title(title)

    if save_path:
        plt.savefig(save_path, transparent=True)

    plt.show()