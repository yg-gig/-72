import os
import pygame
import speech_recognition as sr
import pyautogui as pg
from pygame.time import delay
import pyttsx3
# obtain audio from the microphone
r = sr.Recognizer()
engine = pyttsx3.init()
s =1
l =1
m =2

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("готов к работе")
while s==1:
    with sr.Microphone() as source:

        audio = r.listen(source)

    try:

        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        a =r.recognize_google(audio, language='ru-RU')

        if a == 'Яндекс':
            pg.click(613, 1153, duration=0.5)
            pg.typewrite('yandex', 0.5)
            pg.click(679, 208, duration=0.5)
            speak("яндекс открыт")

        if a == 'Сохранить':
            pg.hotkey('ctrl', 's')
        if a =='Копировать':
            pg.hotkey('ctrl', 'c')

        if a=='Вставить':
            pg.hotkey('ctrl', 'v')
        if a=='назад':
            pg.hotkey('ctrl','z')
            speak("возвращенно")
        if a == 'язык':
            pg.hotkey('alt', 'shift')
            speak('язык был поменят')
        if a == 'Arduino':
            pg.click(613, 1153, duration=0.5)
            pg.typewrite('arduino', 0.5)
            pg.click(679, 208, duration=0.5)
            speak("ардуино открыто")
        if a == 'Pay char':
            pg.click(613, 1153, duration=0.5)
            pg.typewrite('PyCharm Com', 0.5)
            pg.click(679, 208, duration=0.5)
            speak("пайчарм открыт")



            delay(1000)
            print('j')
        if a =='свернуть':
            pg.click(1729, 0, duration=0.5)
            speak("свёрнуто")
        if a =='закрыть':
            pg.click(1865, 23, duration=0.5)
            speak("закрыто")
        if a =='выключить':
            pg.click(1451, 39, duration=0.5)

        if a=='питание':
            pg.typewrite('pinMode');pg.typewrite('();')
            speak("пинмод написан")
        if a == 'печатать в Word':
            pg.click(613, 1153, duration=0.5)
            pg.typewrite('Word', 0.5)
            pg.click(679, 208, duration=0.5)
            speak("ворд открыт")
        if a == 'печатать':
            pg.click(613, 1153, duration=0.5)
            m =2
        if a == 'Enter':
            pg.typewrite(['enter'])
            speak("энтр был нажат")



    except sr.UnknownValueError:
        print("Google ошибка")
    except sr.RequestError as e:
        print("ошибка".format(e))
