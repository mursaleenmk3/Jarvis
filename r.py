from msilib.schema import Class
from threading import main_thread
from time import time
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
from requests import get
from wikipedia import exceptions
import pyjokes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jgui import Ui_Widget
import sys





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("jarvis activated")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell dear how may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sender_email@gmail.com", "password")
    server.sendmail("recevier_email", to, content)
    server.close()




class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()  


    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language="en-in")
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return self.query


    def TaskExecution(self):

        wishMe()
        while True:
  
         self.query =self.takeCommand().lower()

        # Logic for executing tasks based on query
         if "wikipedia" in self.query:

            speak("Searching Wikipedia...")
            self.query =self.query.replace("wikipedia", "")
            results = wikipedia.summary(self.query, sentences=2)

            speak("According to Wikipedia")

            print(results)
            speak(results)
         elif "how are you" in self.query:
             speak("I am doing well and you")    

         elif "open youtube" in self.query:
            webbrowser.open("youtube.com")
            speak("ok")
         elif "play online music" in self.query:
            webbrowser.open("https://gaana.com/song/sare-jahan-se-accha-8")
            speak("ok")

         elif "open facebook" in self.query:
            webbrowser.open("facebook.com")
            speak("ok")

         elif "open instagram" in self.query:
            webbrowser.open("instagram.com")
            speak("ok")

         elif "open google" in self.query:
            webbrowser.open("google.com")
            speak("ok")

         elif "open stackoverflow" in self.query:
            webbrowser.open("stackoverflow.com")
            speak("ok")

         elif "play music" in self.query:
            webbrowser.open("https://youtu.be/5ahXODbIPxc")
            speak("ok mam")
           

         elif "the time" in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

         elif "open vs code" in self.query:
            codePath = "C:\\Users\\Mursaleen\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("ok ")
            os.startfile(codePath)

         elif "open notepad" in self.query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            speak("ok ")
            os.startfile(npath)
         elif "open task manager" in self.query:
            tpath = "C:\\Windows\\system32\\taskmgr.exe"
            speak("ok ")
            os.startfile(tpath)
         elif "open cmd" in self.query:
            speak("ok")
            os.system("start cmd")
         elif "tell me a joke" in self.query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

         elif "ip address" in self.query:
            ip = get("https://api.ipify.org").text
            speak("ok mam ")
            speak(f"your ip address is {ip}")
            print(f"your ip address is {ip}")

         elif "send message" in self.query:
            kit.sendwhatmsg("mobile_number", "hii how are you", -0, 1)

         elif "email to someome" in self.query:
            try:
                speak("What should I say?")
                content = self.takeCommand()
                to = "recevier email"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")

         elif "note it" in self.query:
            try:
                r = sr.Recognizer()
                speak("yes speek")
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=5)
                    print("Recognizing")
                    text = r.recognize_google(audio_data)
                    print(text)
            except Exception as e:
                print(e)
                speak("sorry not recognized plase speek again")
                print("sorry not recognized plase speek again")
         elif "close notepad" in self.query:
            try:
                speak("yes closing notepad")
                os.system("TASKKILL /F /IM notepad.exe")
            except exceptions as e:
                print(e)
                print("it is already closed")
         elif "close vs code" in self.query:
            try:
                speak("yes mam closing vscode")
                os.system("TASKKILL /F /IM Code.exe")
            except exceptions as e:
                print(e)
                print("it is already closed")
         elif "close youtube" in self.query:
            try:
                speak("yes mam closing ")
                os.system("TASKKILL /F /IM msedge.exe")

            except exceptions as e:
                print(e)

startExce=MainThread()

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()  
        self.ui=Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.setWindowTitle("Jarvis")
    def startTask(self):
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/border.gif")  
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/d2.gif")  
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
      
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/world1.gif")  
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/d2.gif")  
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/run.gif")  
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/d3.gif")  
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/d5.gif")  
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/d1.gif")  
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/d4.gif")  
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/run.gif")  
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../new_jarvis/img/output-onlinegiftools.gif")  
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExce.start()
    def showTime(self):
        C_time=QTime.currentTime()
        now=QDate.currentDate()
        l_time=C_time.toString('hh:mm:ss')
        l_date=now.toString(Qt.ISODate)
        
        self.ui.textBrowser.setText("Listening...")
        self.ui.textBrowser_4.setText(l_date)
        self.ui.textBrowser_2.setText(l_time)




app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
sys.exit(app.exec())



