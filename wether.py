import requests

open_weather_token = "2f1661c0fda350128a88e807bc745ba8"
city = 'Helmond'
def get_weather(city, open_weather_token):
    code_4_smile= {
        'Clear': 'Ясно \U00002600',
        'Clouds':"Хмарно \U00002601",
        'Rain':"Дощ \U00002614 \n\nБери дощовик\U0001F302",
        'Drizzle':"Дощ \U00002614 \n\nБери дощовик\U0001F302",
        'Thunderstorm': "Гроза \U000026C8",
        'Snow': "Сніг \U0001F328\n\nВдягайся тепліше\U0001F9E3",
        'Mist': "Туман \U0001F32B\n\nБаба нічого не бачить"
    }
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data = r.json()


        misto= data['name']

        a=data['weather']
        b=a[0]
        weather= b['main']
        if weather in code_4_smile:
            wd = code_4_smile[weather]
        else:
            print('Баба не бачить погоду')

        temperature = data['main']['temp']
        vlazhnost = data['main']['humidity']
        wind= data['wind']['speed']
        res=(f'В місті {misto} зараз {temperature} градусів Цельсію\nЗа вікном {wd}\nВологість: {vlazhnost} відсотків\nШвидкість вітру {wind} м.с ')
        return res


    except Exception as ex:
        print ('ex')

# fir='aaa'
# b='sadsad'



