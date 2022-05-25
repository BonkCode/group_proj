# перед работой ввести код в терминале:
# pip install --upgrade PySimpleGUI
# pip install --upgrade pillow

import PySimpleGUI as pg
import numpy as np
import pandas as pd
from typing import Optional
from typing import List
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import io
from graph2 import plot_barplot_figure
# data
option_plots = ['Пример',
                'Гендерная структура заёмщиков',
                'Количество мужчин-заёмщиков в разрезе стран',
                'Количество групп-заёмщиков в разрезе стран',
                'Количество займов в разрезе стран',
                'Количество займов в разрезе деятельности',
                'Рейтинг 15 целевых назначений для займа',
                'Количество займов в разрезе макро-регионов',
                'Минимальная и максимальная сумма займа по сектору',
                'Сумма займа для каждой страны по полу заёмщика',
                'Количество дней до полного финансирования заявки',
                'Время ожидания и суммы займов',
                'Время ожидания и секторы экономики',
                'Время погашения кредита заёмщиком']


# thumbnail function
def img_thumb(img):
    img.thumbnail((400, 400))
    name = io.BytesIO()
    img.save(name, format="PNG")
    return name


def upload_file(window: pg.Window, file_path: str) -> Optional[pd.DataFrame]:
    df_main = None
    try:
        df_main = pd.read_csv(file_path)
    except FileNotFoundError:
        print('ERROR: FILE NOT FOUND')
        return None
    dataframe_columns = []
    for column in df_main.columns:
        dataframe_columns.append(column)
    window['-O-MENU-X-'].Update(values=dataframe_columns)
    window['-O-MENU-Y-'].Update(values=dataframe_columns)
    return df_main


def get_data(dataframe: pd.DataFrame, x_column_name: str, y_column_name: str) -> Optional[pd.DataFrame]:
    if x_column_name == '' or y_column_name == '':
        return None
    data = dataframe[[x_column_name, y_column_name]]
    data.columns = ['x', 'y']
    return data


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def setup_layout() -> List:
    layout = [
        [pg.Text('Выберите x:'), pg.OptionMenu(values=['Empty'], key='-O-MENU-X-'), pg.Text('Выберите y:'),
         pg.OptionMenu(values=['Empty'], key='-O-MENU-Y-')],
        [pg.Text('Введите название файла с данными: '), pg.InputText(key='-TEXT-BOX-')],
        [pg.Radio('Круговая диаграмма', 'plot', default=True, key='-CIRCLE-'),
         pg.Radio('Столбчатая диаграмма', 'plot', key='-BAR-'),
         pg.Radio('Точечная диаграмма', 'plot', key='-POINT-')],
        [pg.Canvas(key='-GRAPH-CANVAS-')],
        [pg.Button('Показать график'), pg.Button('Загрузить файл')]
    ]
    return layout


def test_draw(data):
    fig = plt.figure()
    plt.plot(data['x'], data['y'])
    return fig


if __name__ == '__main__':
    pg.theme('Kayak')
    # layout
    layout = setup_layout()
    window = pg.Window('Построение графика по csv файлу', layout, finalize=True)
    # event loop
    file_path = None
    df_main = None
    drawn_figure = None
    while True:
        event, values = window.read()
        file_path = values['-TEXT-BOX-']
        if event == pg.WIN_CLOSED:
            break
        elif event == 'Загрузить файл' and file_path is not None:
            df_main = upload_file(window, file_path)
        elif event == 'Показать график' and df_main is not None:
            if drawn_figure is not None:
                drawn_figure.get_tk_widget().forget()
                plt.close('all')
            data = get_data(df_main, values['-O-MENU-X-'], values['-O-MENU-Y-'])
            if data is None:
                continue
            print(data.columns)
            data = data.head(5)
            fig = test_draw(data)
            drawn_figure = draw_figure(window['-GRAPH-CANVAS-'].TKCanvas, fig)
    # closing the window
    window.close()
