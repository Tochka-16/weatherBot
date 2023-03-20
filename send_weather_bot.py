from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, WEATHER_API
import requests
from deg_check import determineWind


bot = Bot(TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands='start')
async def startingMessage (msg: types.Message) -> None:
    await msg.reply (text = 'Привет! Чтобы получить погоду, введи название интересующего тебя города <b>(rus/eng)</b>.',
                    parse_mode = 'HTML')

@dp.message_handler()
async def getWeather(msg: types.Message):
    try:
        weather = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={msg.text}&appid={WEATHER_API}&units=metric"
        )
        data = weather.json()

        city = data["name"]
        temp = data["main"]["temp"]
        wind_spd = data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]

        detWind = str(determineWind(float(wind_deg)))

        await msg.reply (text = f"<b>Погода в городе</b>: {city}\n"
                                f"<b>Скорость ветра</b>: {wind_spd}м/с\n<b>Направление ветра</b>: {detWind}\n"
                                f"<b>Температура</b>: {temp}C°", 
                        parse_mode = 'HTML'
                        )

    except:
        await msg.reply ("Точно правильно ввели??")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)