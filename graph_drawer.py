import PySimpleGUI as pg
import pandas as pd
from typing import Optional
from typing import List
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from karemina_barchart import plot_barplot_figure
from layout import Layout


class GraphDrawer:
    class EventHandler:
        def __init__(self):
            pass

        @staticmethod
        def handle(parent, window, event: str, values) -> int:
            if event != pg.WIN_CLOSED:
                parent.file_path = values['-TEXT-BOX-']
            if event == pg.WIN_CLOSED:
                return -2
            elif event == 'Загрузить файл' and parent.file_path is not None:
                parent.upload_file(window, parent.file_path)
            elif event == 'Показать график' and parent.df_main is not None:
                parent.draw(window=window, values=values)
            return 0

    def __init__(self):
        self.file_path = None
        self.df_main = None
        self.drawn_figure = None
        self.event_handler = self.EventHandler()

    def draw(self, window, values):
        if self.drawn_figure is not None:
            self.drawn_figure.get_tk_widget().forget()
            plt.close('all')
        # getting data
        try:
            data = GraphDrawer.get_data(self.df_main, values['-O-MENU-X-'], values['-O-MENU-Y-'])
        except Exception as e:
            print(f'ERROR: {str(e)}')
            return
        # plotting graph
        try:
            fig = plot_barplot_figure(data)
            self.draw_figure(window['-GRAPH-CANVAS-'].TKCanvas, fig)
        except Exception as e:
            print(f'ERROR: {str(e)}')
            return

    @staticmethod
    def test_draw(data):
        fig = plt.figure()
        plt.plot(data['x'], data['y'])
        return fig

    def draw_figure(self, canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        self.drawn_figure = figure_canvas_agg

    @staticmethod
    def get_data(dataframe: pd.DataFrame, x_column_name: str, y_column_name: str) -> Optional[pd.DataFrame]:
        class ColumnNameError(Exception):
            pass

        if x_column_name == '' or y_column_name == '':
            raise ColumnNameError("Column name(s) is(are) empty!")
        data = dataframe[[x_column_name, y_column_name]]
        data.columns = ['x', 'y']
        return data

    def upload_file(self, window: pg.Window, file_path: str) -> Optional[pd.DataFrame]:
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
        self.df_main = df_main
