import datetime
from makedic import Makedic
from pyowm import OWM

API_key = ''
owm = OWM(API_key=API_key)

class Functions:
    def off_light(self):
        return "off_light 아직 라즈베리가 없어요"

    def on_light(self):
        return "on_light 아직 라즈베리가 없어요"

    def time(text):
        day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        if text=='요일':
            r = datetime.datetime.today().weekday()
            return day[r]
        else:
            return "time "+str(datetime.datetime.now())

    def weather(self):
        obs = owm.weather_at_coords(37.4386, 127.1378)
        w = obs.get_weather()
        l = obs.get_location()
        return l.get_name()+" : "+w.get_status()+", "+str(w.get_temperature(unit='celsius')['temp'])+"°"
    
    def update(self):
        up = Makedic()
        up.writefile()
        return "업데이트 완료"