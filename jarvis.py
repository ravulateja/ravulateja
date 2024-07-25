import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
import random
from requests import get # this is also used for ip addres of a particular ip aadress for https:// api.ipify.org
import socket #socket helps us to perform dns lookups
import dns.resolver
import wikipedia
import pywhatkit as whats
import smtplib #for sending email 
import sys
import re
import pyjokes
import time
import pyautogui# used to programatically conterol the keys and the mouse


engine = pyttsx3.init('sapi5')
'''SAPI5 on Windows XP and Windows Vista and Windows 8,8.1 , 10 NSSpeechSynthesizer on Mac OS X 10.5 (Leopard) and 10.6 (Snow Leopard)espeak on Ubuntu Desktop Edition 8.10 (Intrepid), 9.04 (Jaunty), and 9.10 (Karmic)'''
voices = engine.getProperty('voices')
#print(voices[0].id) o,1 are the ids of voice actors
engine.setProperty('voices',voices[0].id)                                                                                                                                                   

def speak(audio):

    """
    This function uses the text-to-speech engine to speak the provided audio input.
    
    Args:
    audio (str): The text to be spoken out loud.
    
    Returns:
    None
    """
    engine.say(audio)
    print(audio)
    engine.runAndWait()



#taking command form the user
def takecommand():
    """
    Function to take user's voice input using the microphone and recognize speech using Google Speech Recognition.

    Returns:
    query (str): The text of the speech input recognized from the user.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=2, phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    
    except Exception as e:
        speak("Say that again please")
        return None
    
    return query
import datetime

def wish():
    """
    Greet the user based on the current time of the day.

    This function gets the current hour using datetime module and greets the user
    with 'good morning', 'good afternoon', 'good evening', or 'good night' based on the time.

    Returns:
    None
    """
    hour = int(datetime.datetime.now().hour)
    print("the time is :", hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour <= 16:
        speak("good afternoon")
    elif hour > 16 and hour <= 21:
        speak("good evening")
    else:
        speak("good night")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)

    server.ehlo()
    server.starttls()
    server.login('thetruths2024@gmail.com','truths@1234')#acconts with 2 step verifcstion will not able to senfd the mail
    server.sendmail('thetruths2024@gmail.com',to,content)
    server.close()


if __name__ == "__main__":

    speak(" I am jarvis, how can i help you")

    while True:
    
        query = takecommand().lower() 

        if "open google" in query:
            path1="https://www.google.com/"
            os.startfile(path1)   
 
        
        
        elif "open notepad" in query:
            path2="C:\\Windows\\notepad.exe"
            os.startfile(path2)
        
        
        
        elif "open camera" in query:
            cap= cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:# 27 is the ascii value of esccape button which closes the capture window
                    break;
            cap.release()
            cv2.destroyAllWindows()

       

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "time" in query:
            speak(f"its {datetime.datetime.now().time()}")
        

        elif "date" in query:
            speak(f"today is {datetime.datetime.now().date()}")

        elif "play music" in query:
            music_dir="C:\\Users\\ravul\Music\\audio"
            songs=os.listdir(music_dir)
            song_num=random.choice(songs)
            os.startfile(os.path.join(music_dir, song_num))
           
            

        elif "play video" in query:
            vid_dir="C:\\Users\\ravul\\Videos\\short film"
            vids=os.listdir(vid_dir)
            vids_dir=takecommand().lower()
            video=vids_dir+".mp4"
            speak(video)
            for i in vids:
                
                if i.lower() in video:
                    speak("loading video......")
                    os.startfile(os.path.join(vid_dir, i))
        

       # elif "ip address" in query:
             
           # speak("sir for which site i must search the ip adress ")
           
           # ip=takecommand().lower()
           
           # ip1 = dns.resolver.resolve(ip,'A')
           # ip_list=[ip.address for ip2 in ip1]
           # ip_addr_str=",".join(ip_list)
           # speak(f"the ip adress of this site is {ip_addr_str}")
            
            
        elif "wikipedia" in query:
            speak("searching in wikipedia")
            sent=query.replace("wikipedia","") #without sent removing the wikipedia aord it also searches the term wikipedia so we must remove the word
            result=wikipedia.summary(sent,sentences=3) #operations we can perform oon wikipedia are summary,page,search.........                    
            print(result)


        elif  "search" in query:
            cmd=query.replace("search for","")
            webbrowser.open(cmd)

        elif "what is" in query:
            webbrowser.open(query)
        

        elif "send message" in query:
            whats.sendwhatmsg("+9398217226", "yooooo whats app popssssss ",11,47)

        elif "songs" in query:
            speak("is there any specific song to play")
            com=takecommand().lower()
            com1=com.replace("play","")
            if "no" in com:
                whats.playonyt("beleiver")

            else:
                whats.playonyt(com1)



        elif "send mail" in query: #we use smtplib library to send mails
                                                                                                                                
                                                                                                                #speak("is there anything i can do sir")
            speak("what should i send")
            content=takecommand().lower()
       
            to='ravulateja12@gmail.com'
            sendEmail(to,content)
            speak("email has been sent")

        elif "terminate" in query:
            speak("bye sir , see you soon")
            sys.exit()

        
        elif "close" in  query:
            program=query[6:]+'.exe'
            os.system(f'taskkill /f /im {program}')

        elif "set alarm" in query:
            hr=int(datetime.datetime.now().strftime('%H:%M'))
            print(hr)
            speak("when should i notify  you u sir")
            time=takecommand().lower()
            check=[]
            hour=re.findall(r'\d+',hour)
            check.append(hour)
            minu=re.findall(r'\d+',min)
            check.append(minu)
            tie=":".join(check)
            if hr[0:2]==tie[0] and hr[2:4]==tie[2]:

            



                music_dir="C:\\Users\\ravul\Music\\audio"
                songs=os.listdir(music_dir)
                song_num=random.choice(songs)
                os.startfile(os.path.join(music_dir, song_num))


        elif "joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)

        elif "shutdown" in query:
            os. system("shutdown /s /t 5")
        elif "restart" in query:
            os.system ("shutdown /r /t 5")  
        
        elif "change window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')



            


             

