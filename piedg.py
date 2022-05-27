import pandas as pd
from matplotlib import pyplot as plt
import pandas.api.types

def plot_pie(data: pd.DataFrame) -> plt.Figure:

    if not pandas.api.types.is_numeric_dtype(data.y.dtype):
        raise ValueError(f'cannot draw pie for non-numeric series Y')

    processed = data.groupby("x", dropna=True).mean()

    labels = processed.index
    sizes = processed.y.values

    figure, axis = plt.subplots()
    axis.pie(sizes, labels=labels, autopct='%1.1f%%')
    axis.axis('equal')

    return figure

