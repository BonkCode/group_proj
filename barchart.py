import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

    def plot_barplot_figure(data: pd.DataFrame) -> plt.Figure:
    from pandas.api.types import is_numeric_dtype
    fig = plt.figure()
    bins = 30
    data = data.dropna()

    if not is_numeric_dtype(data.y.dtype):
        raise ValueError(f'cannot draw bar plot for non-numeric series Y')

    if not is_numeric_dtype(data.x.dtype):
        data = data.groupby('x').mean().sort_values('y')
        if data.x.nunique() > bins:
            data = data.head(30)
            # don't try to plot messy bar plots
            #raise ValueError(f'categorial column {data.x.name} has cardinality higher than {bins}')

        #data = data.groupby('x').mean().sort_values('y')
        plt.barh(data.index, data.y)
        plt.tight_layout()
        return fig

    data_range = (data.x.max() - data.x.min())

    partitions = ((data.x - data.x.min()) / data_range * bins).apply(np.floor)
    data = data.groupby(by=partitions).mean()

    x, y = data.index * data_range / bins + data.x.min(), data.y

    bin_size = data_range / bins / 2
    plt.bar(x, y, width=bin_size)

    return fig