import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

import matplotlib.dates as mdates
import datetime as dt
import csv
import matplotlib as mpl


    dpi = 80
    fig = plt.pie(dpi = dpi, figsize = (512 / dpi, 384 / dpi))
    data = data.dropna()
    mpl.rcParams.update({'font.size': 9})



    if not is_numeric_dtype(data.x.dtype):
        if data.x.nunique() > dpi:
            raise ValueError(f'categorial column {data.x.name} has cardinality higher than {dpi}')

        data = data.groupby('x').mean().sort_values('y')
        plt.pie(data.index, data.y, autopct='%.1f', radius = 1.1)
        return fig

    data_range = (data.x.max() - data.x.min())

    partitions = ((data.x - data.x.min()) / data_range * dpi).apply(np.floor)
    data = data.groupby(by=partitions).mean()

    x, y = data.index * data_range / dpi + data.x.min(), data.y

    bin_size = data_range / dpi / 2
    plt.pie(x, y, width=bin_size)

    return fig