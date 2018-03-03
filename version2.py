import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule
import urllib3
import urllib
import urllib2
from bs4 import BeautifulSoup
import time
from gtts import gTTS
#import MySQLdb
import sys

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
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)

    
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'DBLS powering off in 3, 2, 1, 0']
            speekmodule.speek(rand,n,mixer)
            break
            
        if ('hello') in message or ('hi') in message:
            rand = ['Wellcome to DBLS virtual intelligence bot. what can i do for you sir.']
            speekmodule.speek(rand,n,mixer)

        if  ('*') in message:
            rand = ['Be polite please']
            speekmodule.speek(rand,n,mixer)

        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            speekmodule.wifi()
            rand = ['We are connected']
            speekmodule.speek(rand,n,mixer)
            
        if ('.com') in message :
            rand = ['Opening' + message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speekmodule.speek(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')

        if ('youtube') in message :
            rand = ['Opening' + message]
            speekmodule.speek(rand,n,mixer)
            query = urllib.quote(message)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib2.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html)
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                print 'https://www.youtube.com' + vid['href']
                Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                webbrowser.get(Chrome).open('https://www.youtube.com' + vid['href'])
                break;

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            speekmodule.speek(rand,n,mixer)

        if message != ('start music') and ('start') in message:   
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            speekmodule.speek(rand,n,mixer)
            
        if message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            speekmodule.speek(rand,n,mixer)

        if ('speech to text') in message:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                n=(n+1)     
                print("Speak a sentence!")
                audio = r.listen(source)
                s = (r.recognize_google(audio))
                message1 = (s.lower())
                print (message1)
                f = open('helloworld.txt','w')
                f.write(message1)
                f.close()        
                

        if ('text to speech') in message:
            text1 = raw_input("Type text here : ")
            tts = gTTS(text=text1 , lang='en', slow=True)
            tts.save("texttospeech.mp3")
            os.system("texttospeech.mp3")
            time.sleep(3)
            
        if ('stop music') in message:
            os.system('taskkill /im vlc.exe /f')
            rand = ['stopping music']
            speekmodule.speek(rand,n,mixer)

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speekmodule.speek(rand,n,mixer)
            os.system('python -m pip install ' + result)

        if ('sleep mode') in message:
            rand = ['good night']
            speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('play song') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = ['start playing']
            speekmodule.speek(rand,n,mixer)

        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speekmodule.speek(rand,n,mixer)

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))  
