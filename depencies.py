import microphone
import time
import datetime

now = datetime.datetime.now()

if now.hour >= 6 and now.hour < 12:
   microphone.speak("Доброе утро!")
elif now.hour >= 12 and now.hour < 18:
    microphone.speak("Добрый день!")
elif now.hour >= 18 and now.hour < 23:
    microphone.speak("Добрый вечер!")
else:
    microphone.speak("Доброй ночи!")

microphone.listen()