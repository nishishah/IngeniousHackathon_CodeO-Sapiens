import os
import pyaudio
import speech_recognition as sr
#import speekmodule
import urllib3

http = urllib3.PoolManager()

def ai():
    doss = os.getcwd()
    i=0
    n=0
    global status
    while (i<1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.adjust_for_ambient_noise(source)
            n=(n+1)     
            print("Say something!")
            audio = r.listen(source)
            
        try:
            status = 1
            s = (r.recognize_google(audio))
            message = (s.lower())
            print (message)
            message1 = message.replace(" ", "%20")
            baseURL = 'localhost/hack2/mail.php?status=%s&message=\'%s\'' %(status, message1)
            #fin=baseURL +"temp=%s&hum=%s" %(temperature, humidity)
            print baseURL
            f = http.request('GET',baseURL)
            f.close()
   
        except sr.UnknownValueError:
            print("$could not understand audio")
        except sr.RequestError as e:
            print("Could not request results$; {0}".format(e))

while(True):
    ai()
