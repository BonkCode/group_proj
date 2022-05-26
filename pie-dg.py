import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

import matplotlib.dates as mdates
import datetime as dt
import csv
import matplotlib as mpl


def pie_figure(data: pd.DataFrame) -> plt.Figure:
    from pandas.api.types import is_numeric_dtype
    

    fig1, ax1 = plt.subplots()
    ax1.axis('equal')
    ax1.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

    bins = 30
    fig = plt.pie()
    fig1 = fig
    data = data.dropna()


    if not is_numeric_dtype(data.y.dtype):
        raise ValueError(f'cannot draw bar plot for non-numeric series Y')

    if not is_numeric_dtype(data.x.dtype):
        if data.x.nunique() > bins:
            raise ValueError(f'categorial column {data.x.name} has cardinality higher than {bins}')

        data = data.groupby('x').mean().sort_values('y')
        plt.pie(data.index, data.y)
        plt.tight_layout()
        return fig

    data_range = (data.x.max() - data.x.min())

    partitions = ((data.x - data.x.min()) / data_range * bins).apply(np.floor)
    data = data.groupby(by=partitions).mean()

    x, y = data.index * data_range / bins + data.x.min(), data.y

    bin_size = data_range / bins / 2
    plt.pie(x, y, width=bin_size)

    return fig
