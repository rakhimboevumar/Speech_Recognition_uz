from django.shortcuts import render
import speech_recognition as sr
import pyaudio
import playsound
import os
import sys
import webbrowser
import random
from time import ctime
from gtts import gTTS
import requests

def button(request):
    return render(request, 'home.html')

def output(request):
    

    mic = sr.Microphone(device_index = 1)

    list_mic = sr.Microphone.list_microphone_names()
    for i in range(0,len(list_mic)):
        print(i, list_mic[i])
        
    r=sr.Recognizer()
    with mic as source:
        print('say somthing')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        a=r.recognize_google(audio, language="uz-UZ").capitalize()
        print("Google Speech Recognition thinks you said " + a)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    # a=a.text
    return render(request, 'home.html', {'a':a})