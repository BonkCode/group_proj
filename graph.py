from barchart import plot_barplot_figure
from piedg import plot_pie
from scatterdg import plot_scatter
import pandas as pd
from matplotlib import pyplot as plt


class Graph:
    @staticmethod
    def plot_figure(data: pd.DataFrame):
        pass


class BarGraph(Graph):
    @staticmethod
    def plot_figure(data: pd.DataFrame) -> plt.Figure:
        return plot_barplot_figure(data)


class PieGraph(Graph):
    @staticmethod
    def plot_figure(data: pd.DataFrame) -> plt.Figure:
        return plot_pie(data)


class ScatterGraph(Graph):
    @staticmethod
    def plot_figure(data: pd.DataFrame) -> plt.Figure:
        return plot_scatter(data)
