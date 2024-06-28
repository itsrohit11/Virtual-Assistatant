import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
from openai import OpenAI
from gtts import gTTS


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "8d0398b6ab974f40980dca2f9606738a"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')


    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running to let the music play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open("https://google.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("https://youtube.com")
    elif 'open facebook' in c.lower():
        webbrowser.open("https://facebook.com")
    elif 'open instagram' in c.lower():
        webbrowser.open("https://instagram.com")
    elif 'open twitter' in c.lower():
        webbrowser.open("https://twitter.com")
    elif 'open whatsapp' in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif 'open gmail' in c.lower():
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    elif 'open linkedin' in c.lower():
        webbrowser.open("https://www.linkedin.com/in/rohit-jain-a92ba8256/")
    elif 'open github' in c.lower():
        webbrowser.open("https://github.com")
    elif 'open leetcode' in c.lower():
        webbrowser.open("https://leetcode.com/u/itsrohit11/")
    elif 'open My equation' in c.lower():
        webbrowser.open("https://learn.myequation.in/myaccount/#/course/101645/lesson/905999?lesson=905999&lesson_type=material&section=253199&subject=270314")
    elif 'open spotify' in c.lower():
        webbrowser.open("https://open.spotify.com/?trackId=3eSm4iAkLsn3BeggfiQOH9")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif 'news' in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=8d0398b6ab974f40980dca2f9606738a")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
    # print(c)
    else:
        pass

    


if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        # Listen for the wakeword Jarvis
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word =  r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("yes sir")
                # Listen for command
                with sr.Microphone() as source: 
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command =  r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

