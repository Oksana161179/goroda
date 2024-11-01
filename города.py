from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser

def get_coordinates(city, key):#создаем функцию получения координат:
    # передаем город(название) и ключ
    try:#попробовать
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:#делаем проверку:если все хорошо, возвращает нам информацию
            lat = round(results[0]['geometry']['lat'], 2)#создаем переменную для широты
            # и округляем ее до двух знаков после запятой
            lon = round(results[0]['geometry']['lng'], 2)#создаем переменную для долготы
            # и округляем ее до двух знаков после запятой
            country = results[0]['components']['country']#выводим результаты о стране, в котором находится город
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlot={lon}"#отправляем запрос на сайт карт

            if 'state' in results[0]['components']:#делаем проверку: проверяем, существует ли регион, если да
                region = results[0]['components']['state']#выводим результаты о регионе, в котором находится город
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}.\n Регион: {region}",
                    "map_url": osm_url
                        }

                #возвращаем широту, долготу, страну и регион
            else:#если же не существует
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}.",
                    "map_url": osm_url
                        }
        else:#если же ничего нет
            return "Город не найден"#то возвращается сообщение об этом
    except Exception as e:#обрабатываем исключения
         return f"Возникла ошибка: {e}"#возвращается сообщение об ошибке

def show_coordinates(event=None):#создаем функцию, которая будет вызываться после нажатия на кнопку
    global map_url
    city = entry.get()#получаем название города из поля ввода
    result = get_coordinates(city, key)#создаем переменную-coordinates, в которую положим вызов функции.
    # а передаем в ней город и ключ
    label.config(text=f"Координаты города {city}:\n {result['coordinates']}")#конфигурируем кнопку
    map_url = result['map_url']

def show_map():#создаем функцию показа города на карте, которая привязана к кнопке
    if map_url:#и если карта существует, если этот путь не пустой
        webbrowser.open(map_url)# тогда мы открываем карту

key = 'fb6b2a8e60d74ae397a69757e0b1f27b'
map_url = ""

window = Tk()#создаем окно
window.title("Координаты городов")#задаем заголовок окну
window.geometry("320x160")#задаем размер окну

entry = Entry()#создаем поле ввода
entry.pack()
entry.bind("<Return>", show_coordinates)#чтобы кнопка нажималась с помощью кнопки-Enter с клавиатуры
# и вызываем функцию-show_coordinates

button = Button(text="Поиск координат", command=show_coordinates)#создаем кнопку
button.pack()

label = Label(text="Введите город и нажмите на кнопку")#создаем метку
label.pack()

map_button = Button(text="Показать карту", command=show_map)#создаем кнопку
map_button.pack()



window.mainloop()


