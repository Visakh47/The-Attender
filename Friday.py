#Visakh's FRIDAY AI Program

import pyttsx3 # pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime 
import wikipedia 
import webbrowser 
import os 
import random
#use conda install -c anaconda pyaudio 
engine = pyttsx3.init('sapi5') #sapi5 for windows - engine
voices = engine.getProperty('voices') #returns a list of voices 

#print(voices[0].id) for male voice 
print(voices[1].id)


engine.setProperty("voice",voices[1].id)
engine.setProperty('rate', 190)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #process and wait till audio is finished



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good Morning Sir ')
    elif (hour>=12 and hour<18):
        speak('Good Afternoon Sir')
    else :
        speak('Good Evening')
        
    speak(' I am Friday , Your Virtual Assistant , Please tell me how can i help you ')

#if __name__wishME().n__':
   # wishMe()

def takeCommand():
    # It takes microphone input from the user and returns string output, microphone input requires PyAudio - ​pip install pipwin , pipwin install pyaudio
    
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        a.pause_threshold =1 #1 second gap during speech
        a.energy_threshold =300 # minimum audio wave amplitude/energy
        a.adjust_for_ambient_noise(source , duration =1) #dynamically adjust the energy thereshold 
        audio = a.listen(source)  

        try:
            print('Recongnizing...')
            query = a.recognize_google(audio, language='en=us')
            print(f'User Said: {query}\n') #when we are using variable we have to use with f' so the voice reads the value of the variable
        except Exception as e:
            print(e)
            print("Say that again please...")
            query = takeCommand().lower() #converts the command to lower case - recursion is used here in case of error while taking command 
            return query
        return query


def LaptopSleep():
    choice=input("Are you sure you want to put PC to sleep?(y/n)")
    if choice=='n':
        return
    else : #turn hiberantion mode off by executing command : Powercfg -H OFF in powershell 
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") #os.system(string) - it actually executes the string in a windows powershell
        exit(0)


if __name__ == '__main__': 
    wishMe()
    while True :
        query = takeCommand().lower()
        #always write queries in lower case , so it can easily be recognized
        if 'your name' in query:
            speak('My Name Is Friday')
        elif 'hello' in query:
            wishMe()
        elif 'who are you' in query:
            speak('I am FRIDAY - Female Replacement Intelligent Digital Assistant Youth Working For Visakh Bobby , My Creator')
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('Wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According To WikiPedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I  %M  %p")
            speak(f'Sir the time is{strTime}')
        elif 'open code' in query:
            codePath = "C:\\Users\\Vk_57\\Desktop\\Python\\test.py"
            os.startfile(codePath) #Using OS Libraries here
        elif 'spotify' in query:
            spotifypath = "C:\\Users\\Vk_57\Desktop\\Spotify.lnk"
            os.startfile(spotifypath)
        #elif 'open song' in query:
           # music_dir = "C:\\Users\\Vk_57\\Desktop\\Songs"
           # songs = os.listdir(music_dir) //returns all the songs from the directory 
           # os.startfile(os.path.join(music_dir,[random.randrange(0,3)]))
        elif 'my father' in query: 
            speak(" Your Father's Name is Bobby Bhargavan ,Born on April thirtieth ,1971 ,He is 49 Years Old And is currently working as a general physician in Muscat, Oman")           
        elif 'add' in query:
            speak("Enter First Number:")
            num1 = float(input("Enter First Number:"))
            speak("Enter Second Number:")
            num2 = float(input("Enter Second Number:"))
            print(f'Sum = {num1+num2}')
            speak(f'The Addition of {num1} and {num2} is {num1+num2}')
        elif'open facebook' in query:
            webbrowser.open("www.facebook.com", new =2)
        elif 'laptop to rest' in query:
           LaptopSleep()
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com", new =2)
        elif 'exit' in query:
            speak('Goodbye Visakh')
            exit(0)


        
        
        
        