# group_proj

# Полезные ссылки:
https://github.com/smakhijani/kaggle-kiva-crowdfunding/blob/master/Preliminary%20Exploratory%20Data%20Analysis.ipynb
https://nbviewer.org/github/bibliotekue/kiva-microfunds-eda/blob/main/kiva_eda%20%282%29.html

# ВАША ЗАДАЧА
Здесь дублирую то, что вам нужно сделать:
Создаем функцию в отдельном файле, реализуем ее. Прототип описан ниже, вход и выход исключительно такие и никакие иначе.
Ваша задача - написать группировку по X среднего значения(groupby('x').mean(), или что то типа того, не помню точно как в коде выглядеть должно)
```py
def plot_GRAPHTYPE_figure(data: pd.DataFrame) -> plt.Figure:
    fig = plt.figure()
    # Тут крутим данные. Ну там groupby() там и прочее
    plt.plot(data['x'], data['y'])
    return fig
```

После всего, впихните свою функцию в соответствующий класс в файле graph.py(по аналогии с BarGraph):
![image](https://user-images.githubusercontent.com/62333148/170474229-326e2ed1-15f1-471a-9e86-f6160a3a08dd.png)

# Проверка работы вашей части
Я всю интеграцию запилил, так что см. выше.
После того, как сделаете что там написано, прото запускаете(см. ниже)

# Использование программы
![image](https://user-images.githubusercontent.com/62333148/169783978-6642e66b-3865-4c2c-b06d-512d0a582f5b.png)

## Сначала вводим путь к файлу(глобальный, или относительно папки запуска)
![image](https://user-images.githubusercontent.com/62333148/169784544-6a5311b7-55ba-4ed0-ba54-36967164bafc.png)

## Далее жмем на кнопку загрузки файла
![image](https://user-images.githubusercontent.com/62333148/169784703-696938cd-55d2-45db-b2bb-8f40c731d0b3.png)

## Затем выбераем столбцы x и y, которые хотим отобразить на графике и выбираем тип графика
![image](https://user-images.githubusercontent.com/62333148/169784865-f8e50826-cf79-4574-95fd-638cc0679f0b.png)
![image](https://user-images.githubusercontent.com/62333148/170474523-7b83a7fb-96d2-4e78-8f46-2cd402defebc.png)


## И наконец жмем на кнопку "Показать график" и готово!
![image](https://user-images.githubusercontent.com/62333148/169785038-fef1e6c6-ba08-4916-917e-0d07a18b1334.png)
