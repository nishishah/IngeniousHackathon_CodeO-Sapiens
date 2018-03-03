import os
import pyaudio
import speech_recognition as sr
import speekmodule

def ai():
    doss = os.getcwd()
    i=0
    n=0
    while (i<1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.adjust_for_ambient_noise(source)
            n=(n+1)     
            print("Say something!")
            audio = r.listen(source)
            
        try:
            s = (r.recognize_google(audio))
            message = (s.lower())
            print (message)
   
        except sr.UnknownValueError:
            print("$could not understand audio")
        except sr.RequestError as e:
            print("Could not request results$; {0}".format(e))

while(True):
    ai()
