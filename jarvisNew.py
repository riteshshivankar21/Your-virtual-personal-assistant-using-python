import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import pyowm
import webbrowser
import os
import smtplib
import wolframalpha 
from random import randint
import psutil
import platform
import time


def get_size(bytes, suffix="B"):
    
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def WishMe():

    time =int(datetime.datetime.now().hour)
    #print(time)
    if time>=0 and time <12:
        Speak("good Morning")
    elif time >=12 and time <17:
        Speak("good afternoon")

    else:
        Speak("good evening")

    Speak("I am a jarvis Sir ")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
    
        r.pause_threshold = 0.5
        r.energy_threshold = 300 
        audio = r.listen(source)

    try:
        print("recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said {query}\n")

    except Exception as e:
        print("Sorry sir , i can't recognize , please call me again")
        Speak("Sorry sir , i can't recognize , please call me again")
        return "None"

    return query



def Demo():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r1.energy_threshold = 300 
        r1.pause_threshold = 0.5
        audio0 = r1.listen(source)

    try:
        print("recognizing.....")
        query0 = r1.recognize_google(audio0,language='en-in')
        print(f"user said {query0}\n")

    except Exception as e:
        print(e)
        #print("Sorry,Say that again please")
        #Speak("Sorry sir ,  Say that again please")
        return "None"

    return query0


def sendEmail(to, content):
    password = open("E:\Ritesh\pass\pass.txt" , "r")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shivankarritesh@gmail.com', password.read())
    server.sendmail('shivankarritesh@gmail.com', to, content)
    server.close()


def removeSpace(str):
    change_str = ''
    for i in range(len(str)):
        if (str[i] != " "):
            change_str += str[i]
    #print(change_str)
    return change_str
    
        
        



if __name__ == "__main__":
#Speak("Gooooood Morning Boss")
    WishMe()
    
    while True:
        query0 = Demo().lower()
        if "hey jarvis" in query0 or "hi jarvis" in query0 or "jarvis" in query0:
            print("Hii sir , how may i help you")
            query0 = ''
            
            
            Speak("Hii sir , how may i help you")
            query = TakeCommand().lower()
            

            if "wikipedia" in query :
                    Speak("Searching Wikipedia.....")
                    query = query.replace('wikipedia','')
                    results = wikipedia.summary(query,sentences=2)
                    Speak("According to wikipedia..")
                    print(results)
                    Speak(results)
                    query=""
                    
                
            elif "weather" in query or "temperature" in query:
                    own = pyowm.OWM('014f21636d4a923e41285d122c93a046')
                    if "nagpur" in query:
                        location = own.weather_at_place("nagpur")
                        weather = location.get_weather()
                        query = weather.get_temperature('celsius')

                    else:
                        Speak("from which place")
                        place = TakeCommand().lower()
                        location = own.weather_at_place(place)
                        weather = location.get_weather()
                        query = weather.get_temperature('celsius')

                    humidity = weather.get_humidity()
                    Speak(" sir... ,today's temperature is ")
                    print(query)
                    Speak(query)
                    
                    query=""
                    

            elif "google.com" in query or "google" in query:
                    webbrowser.open_new("http://www.google.com")

            elif "youtube.com" in query or "youtube"  in query:
                    webbrowser.open_new("http://www.youtube.com")

            elif "gmail.com" in query or "gmail" in query:
                    webbrowser.open_new("http://www.gmail.com")


            elif 'play' in query:
                    music_dir = 'E:\\Music\\new'
                    songs = os.listdir(music_dir)
                    for i in songs:
                          print(i)
                    length = len(songs)-1
                    no = randint(0, length)
                    Speak("Here is the some songs for you")
                    os.startfile(os.path.join(music_dir, songs[no]))

            elif "stop music" in query or "stop songs" in query:
                os.system("TASKKILL /F /IM VLC.exe")
                Speak("music is stop.......")




            elif 'send email' in query or 'send mail' in query:

                try:
    
    
                    Speak("what is the username of Receiver.....")
                    print("what is the username of Receiver.....")
                    my_str = TakeCommand().lower()
                    
                    to = removeSpace(my_str)
                    print(to)
    
                    if my_str!="":

                        Speak("What should I say?")
                    
                        content = str(TakeCommand())
                        
                        sendEmail(to, content)
                        Speak("Email has been sent!")
                    else:

                        break
                except Exception as e:
                    print(e)
                    Speak("Sorry ") 

            













            elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")



            elif "calculate" in query or "solve" in query or "who is" in query:
                
                    			
                    app_id = "JPJEKA-HRVUJAY9KT"
                    client = wolframalpha.Client(app_id) 
                    
                    res = client.query(query) 
                    answer = next(res.results).text
                    print(answer)
                    Speak("The answer is " + answer)
                    #assistant_speaks("The answer is " + answer) 



            elif "system information" in query:
                    print("="*40, "System Information", "="*40)
                    Speak("Here is the system information")
                    uname = platform.uname()
                    print(f"System: {uname.system}")
                    print(f"Node Name: {uname.node}")

                    Speak("Here is the CPU Information")
                    print("="*40, "CPU Info", "="*40)
                    # number of cores
                    print("Physical cores:", psutil.cpu_count(logical=False))
                    print("Total cores:", psutil.cpu_count(logical=True))

                    Speak("Here is the Memory information")
                    print("="*40, "Memory Information", "="*40)
                    # get the memory details
                    svmem = psutil.virtual_memory()
                    print(f"Total: {get_size(svmem.total)}")
                    print(f"Available: {get_size(svmem.available)}")
                    print(f"Used: {get_size(svmem.used)}")


            


        
       






     

    



