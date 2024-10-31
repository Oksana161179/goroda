from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):#создаем функцию получения координат:
    # передаем город(название) и ключ
    try:#попробовать
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:#делаем проверку:если все хорошо, возвращает нам информацию
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']#возвращаем долготу и широту
        else:#если же ничего нет
            return "Город не найден"#то возвращается сообщение об этом
    except Exception as e:#обрабатываем исключения
        return f"Возникла ошибка: {e}"#возвращается сообщение об ошибке

key = 'fb6b2a8e60d74ae397a69757e0b1f27b'
city = "London"
coordinates = get_coordinates(city, key)#создаем переменную-coordinates, в которую положим вызов функции.
# а передаем в ней город и ключ
print(f"Координаты города {city}: {coordinates}")#выводим в консоль название города-{city}
# и его координаты-{coordinates}


