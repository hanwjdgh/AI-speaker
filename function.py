import datetime

class Functions:
    def off_light(self):
        return "off_light 아직 라즈베리가 없어요"

    def on_light(self):
        return "on_light 아직 라즈베리가 없어요"

    def time(self):
        return "time "+str(datetime.datetime.now())

    def weather(self):
        return "weather 아직 api가 없어요"    