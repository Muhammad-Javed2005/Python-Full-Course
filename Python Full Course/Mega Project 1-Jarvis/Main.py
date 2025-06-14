import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()
newsapi = "<Your Key Here>"

def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

        # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def aiProcess(command):
    client = OpenAI(
    api_key="<Your Key Here>",
    )
        
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.Give short response please."},
        {"role": "user", "content": command}
    ]
    )


    return completion.choices[0].message.content






def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")

    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")

    elif "open linkdlen" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif c.lower().startwith("play") :
        song = c.lower().replace("play", "")
        # song = c.lower.spilt("")[1]
        link = musicLibrary.musics(song)
        webbrowser.open(link)


    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else :
        # Let OpenAI handle the request 
        output = aiProcess(command)
        speak(output)
        
    
    



if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the default microphone
        r=sr.Recognizer()


        # Recognize speech using Sphinx
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Please say the wake word: Jarvis")
                audio = r.listen(source , timeout = 2 , phrase_time_limit = 1)
            word = r.recognize_google(audio)
            print(word)

            if (word.lower() == "jarvis"):
                speak("Yah..")
                # listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active:")
                    audio = r.listen(source) 
                    command = r.recognize_google(audio)

                    processCommand(command)



        except Exception as e :
            print("Error; {0}".format(e))



    
