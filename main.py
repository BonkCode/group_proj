# перед работой ввести код в терминале:
# pip install --upgrade PySimpleGUI
# pip install --upgrade pillow

import PySimpleGUI as pg
from layout import Layout
from graph_drawer import GraphDrawer
from graph import *
from logger import BonkLogger


if __name__ == '__main__':
    pg.theme('Kayak')
    # layout
    layout = Layout()
    window = pg.Window('Построение графика по csv файлу', layout.layout, finalize=True)
    drawer = GraphDrawer(graphs={'pie': PieGraph, 'bar': BarGraph, 'scatter': ScatterGraph})
    # event loop
    while True:
        event, values = window.read()
        if drawer.event_handler.handle(drawer, window, event, values) == -2:
            break
    # closing the window
    window.close()
