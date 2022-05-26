from typing import List
import PySimpleGUI as pg


class Layout:
    def __init__(self):
        self.layout = None
        self.setup_layout()

    def setup_layout(self) -> List:
        self.layout = [
            [pg.Text('Выберите x:'), pg.OptionMenu(values=['Empty'], key='-O-MENU-X-'), pg.Text('Выберите y:'),
             pg.OptionMenu(values=['Empty'], key='-O-MENU-Y-')],
            [pg.Text('Введите название файла с данными: '), pg.InputText(key='-TEXT-BOX-')],
            [pg.Radio('Круговая диаграмма', 'plot', default=True, key='-CIRCLE-'),
             pg.Radio('Столбчатая диаграмма', 'plot', key='-BAR-'),
             pg.Radio('Точечная диаграмма', 'plot', key='-POINT-')],
            [pg.Canvas(key='-GRAPH-CANVAS-')],
            [pg.Button('Показать график'), pg.Button('Загрузить файл')]
        ]
