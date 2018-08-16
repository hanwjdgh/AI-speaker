import datetime
from makedic import Makedic

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
        return "weather 아직 api가 없어요"    
    
    def update(self):
        up = Makedic()
        up.writefile()
        return "업데이트 완료"