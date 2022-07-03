import pandas as pd
from matplotlib import pyplot as plt
from logger import BonkLogger


def plot_scatter(data: pd.DataFrame) -> plt.Figure:
    logger = BonkLogger.get_instance()

    processed = data
    head_len = 1000
    if processed.x.nunique() > 15:
        while processed.x.nunique() > 15 and head_len > 50:
            processed = processed.head(head_len)
            head_len -= 50
        logger.info(f'cut the dataframe to new len(was too long before). new len={head_len}')

    figure, axis = plt.subplots()
    axis.scatter(processed.x, processed.y)

    return figure
