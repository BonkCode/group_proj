from karemina_barchart import plot_barplot_figure
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
        from graph_drawer import GraphDrawer
        return GraphDrawer.test_draw(data)


class ScatterGraph(Graph):
    @staticmethod
    def plot_figure(data: pd.DataFrame) -> plt.Figure:
        from graph_drawer import GraphDrawer
        return GraphDrawer.test_draw(data)
