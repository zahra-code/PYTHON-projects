import json  # VIRTUAL ASSISTANT  #tea-rex
import pyttsx3  # for speak function
import speech_recognition as sr
import datetime  # for finding time
import wikipedia  # for searching through wikipedia
import webbrowser  # for opening websites
import urllib  # for perfectly parsing URL_link
import tkinter as tk # for making message box
from tkinter import messagebox
import re
import os
import requests
import pygame #for playing music audio
import random #for randomly playing songs
import smtplib #for sending emails
import time
from newsapi import NewsApiClient #for reading news articles from newsAPI
from datetime import timedelta
from email.message import EmailMessage
from config import SENDER_EMAIL,EMAIL_PASSSWORD
import threading  # for running alarm/reminder in thread with other work

# Setting speak function properties
engine = pyttsx3.init('sapi5')  # sapi5 = microsoft speech API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #ZIRA VOICE
engine.setProperty('rate', 150)


# Making function for speak
def speak(text):
    """Put the message in the TTS queue"""
    engine.say(text)
    engine.runAndWait()
    engine.isBusy()

def show_alert(msg):
    """This function is built for giving message alerts"""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Reminder!", msg)
    root.destroy()
def alarm_alert(msg):
    """This function is built for giving message alerts for alarm"""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    pygame.init()

    file_path = os.path.normpath(
        "C:/Users/SL LAPTOP/Music/Funny Minions Wake Up Alarm 🚨 Ringtone 🎧 _ Minions _ Download Link In Description _ JBRupner.mp3")

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        messagebox.showinfo("Alarm Reminder!", msg)
        pygame.mixer.music.stop()  # Stop the music when the message box is dismissed
    except pygame.error as e:
        messagebox.showerror("Error", f"Could not play the alarm sound: {e}")
    finally:
        root.destroy()
        speak("Alarm off")
def wish_me():
    """This function is created to wish user according to time when he opens TEA-REX."""
    overall_time = datetime.datetime.now()
    time = overall_time.strftime("%I %M %p")
    hour = int(overall_time.strftime("%H"))
    minute = int(overall_time.strftime("%M"))
    second = int(overall_time.strftime("%S"))
    format = overall_time.strftime("%p")
    if 0 <= hour <= 5 and 0 <= minute < 60:
        speak("it's late night")
    elif 6 <= hour < 12 and 0 <= minute < 60:
        speak("GOOD morning")
    elif hour == 12 and minute == 0:
        speak("good NOON")
    elif 12 <= hour < 17 and 0 < minute < 60:
        speak("good afternoon")
    elif 17 <= hour < 24 and 0 <= minute < 60:
        speak("good evening")
    speak("I am tea-rex how may I help you")

def take_command():
    """This function is built for taking voice inputs from user"""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("LISTENING...")
            r.pause_threshold = 1.0
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            try:
                print("Recognizing....")
                query = r.recognize_google(audio, language="en-PK")
                print(f"You said: \"{query}\"\n")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
                return "timeout"
            except sr.RequestError:
                speak("Could not recognize your command")
                print(f"Could not request results from Google Speech Recognition service")
                return "None"
            return query
    except Exception as e:
        print("ERROR:",e)
def tea_rex_age_calculation():
    """Calculating age of tea rex"""
    year= int(datetime.datetime.now().strftime("%Y"))
    month= int(datetime.datetime.now().strftime("%m"))
    date= int(datetime.datetime.now().strftime("%d"))
    year=year-2024
    month=month-6
    date=date-18
    if date < 0:
        previous_month = month - 1 if month > 1 else 12
        previous_month_year = year if month > 1 else year - 1
        previous_month_days = (
                datetime.datetime(previous_month_year, previous_month + 1, 1) - datetime.timedelta(days=1)).day

        date += previous_month_days
        month -= 1
    if month<0:
        year-=1
        month+=12
    speak(f"I was created on 18th jane 2024 on tuesday \nSo my age is {date} days {month} months and {year} years")
def tea_rex():
    """This function is made for providing information about Tea-Rex (Virtual Assistant)"""
    speak("I am Tea-Rex, your virtual assistant created by Zahra Shahid. I am here to help you out.")
def date_time_teller(demand):
    """This function is made for telling time,date,day"""
    overall_time = datetime.datetime.now()
    time = overall_time.strftime("%I %M %p")
    date = overall_time.strftime("%d %B %Y")
    day = overall_time.strftime("%A")
    if "time" in demand:
        speak(f"its {time} right now")
    elif "date" in demand:
        speak(f"its {date}")
    elif "day" in demand:
        speak(f"Today is {day}")
    else:
        speak("sorry could not recognize your command")


def wiki(query):
    """This function is built for searching anything through Wikipedia"""
    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
    print("Searching through Wikipedia...")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(result)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        speak("Could not find any results for your query.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")


def opening_websites(query):
    """Function for opening any website"""
    query1 = query
    query1 = query1.replace("open", "")
    if "web" in query1 or "website" in query1 or ".com" in query1 or "t-rex" in query1:
        query1 = query1.replace("web", "").replace("website", "").replace(".com", "").replace("tea-rex", "").replace(
            "t-rex", "").replace("hey","").replace('hello',"").replace("can","").replace("you","").replace("please","").replace("listen","")
    try:
        webbrowser.open(f"{query1}.com")
    except Exception:
        print(f"Could not open {query1} please give clear instructions")


def search_youtube(query):
    """Function for searching in youtube"""
    query1 = query
    query1 = query1.replace("search", "").replace("google", "")
    if "tea-rex" in query1 or "t-rex" in query1 or "in" in query1:
        query1 = query1.replace("tea-rex", "").replace("t-rex", "").replace("in", "").replace("hey","").replace("can","").replace("you","").replace("please","").replace("hello","")
    encoded_query = urllib.parse.quote(query1)
    search_url = f"https://www.youtube.com/search?q={encoded_query}"
    webbrowser.open(search_url)


def search_google(query):
    """Function for searching in google"""
    query1 = query
    query1 = query1.replace("search", "").replace("google", "")
    if "tea-rex" in query1 or "t-rex" in query1 or "in" in query1:
        query1 = query1.replace("tea-rex", "").replace("t-rex", "").replace("in", "")
    print(query1)
    encoded_query = urllib.parse.quote(query1)
    print(encoded_query)
    search_url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(search_url)

def reminder_alarm(query):
    """Function for setting alarms or reminders.It will clearly tell about how many hours minutes or days are remaining till the alarm to ring."""
    query1 = query
    try:
        query1 = query1.replace("a.m.", "am").replace("p.m.", "pm").replace("a.m", "am").replace("p.m", "pm").replace("set alarm", "").replace("can ","").replace("set an alarm", "").replace("set reminder", "").replace("at", "").replace("about","").replace("for", "").replace('t-rex', "").replace("hey", "").replace("remind me at", "").replace("an", "").replace(":",' ').replace("'o clock", '').replace("o clock", "").replace("clock", '').replace("hello","").replace("listen","").replace("you","").replace("please","").replace("set","").replace(" a ","").replace("the","").replace("an","").replace("for","").replace(" me ","").replace("a ","").replace("at","").replace("reminer","").replace("reminder","").replace("set","").replace("for","")
        # calculating time right now
        query1 = query1.split()
        # storing hour
        alarm_min = 0
        if len(query1)>1:
            if re.findall(r"[0-9]*",query1[0]):
                alarm_hour = query1[0]
            if "am" not in query1[1] and "pm" not in query1[1]:
                alarm_min=query1[1]
        if len(query1)==1:
            if re.findall(r"[0-9]",query1[0]):
                alarm_hour = query1[0]
        if "am" not in query1 and "pm" not in query1:
            print("you want to set alarm for AM or PM")
            alarm_format = take_command()
            alarm_format=alarm_format.lower()
            alarm_format=alarm_format.replace(".","")
        else:
            alarm_format = query1[-1]
        if int(alarm_min) >= 60:
            alarm_min = int(alarm_min) - 60
            alarm_hour = int(alarm_hour) + 1

        # Convert time to 24-hour format
        if alarm_format == "pm" and int(alarm_hour) != 12:
            alarm_hour = int(alarm_hour)+ 12
        elif alarm_format == "am" and int(alarm_hour) == 12 and int(alarm_min)==0:
            alarm_hour = 24
        elif alarm_format == "am" and int(alarm_hour) == 12 and (int(alarm_min)>0 and int(alarm_min)<60):
            alarm_hour = 0

        if int(alarm_hour)<10:
            alarm_hour=f"0{alarm_hour}"
        if int(alarm_min)<10 and len(alarm_min)==1:
            alarm_min=f"0{alarm_min}"

        alarm=f"{alarm_hour} {alarm_min} {alarm_format}"

        # Get current time
        now = datetime.datetime.now()
        # Create alarm time for today
        alarm_time = now.replace(hour=int(alarm_hour), minute=int(alarm_min), second=0, microsecond=0)
        # If alarm time is in the past, set for the next day
        if alarm_time <= now:
            alarm_time += timedelta(days=1)
        # Calculate remaining time until alarm
        remaining_time = alarm_time - now
        remaining_days = remaining_time.days
        remaining_seconds = remaining_time.seconds
        remaining_hours = remaining_seconds // 3600
        remaining_minutes = (remaining_seconds % 3600) // 60
        # Return the alarm time in the original format and remaining time
        speak(f"Alarm is set for {alarm_time.strftime("%I %M %p")}\n{remaining_days} days {remaining_hours} hours and {remaining_minutes} minute remaining.")
        return alarm
    except Exception as e:
        speak(f"Could not set an alarm due to unclear instructions {e}")
def play_music():
    """This function plays music files from a specified directory in a random pattern."""
    path_files = "C:/Users/SL LAPTOP/Music/songs"
    files = os.listdir(path_files)
    if files:
        # Ensure only audio files are considered (filter by extension if necessary)
        files = [file for file in files if file.endswith(('.mp3', '.wav', '.ogg'))]

    if not files:
        print("No audio files found in the directory.")
        return

    pygame.init()
    is_paused = False

    while True:
        if not is_paused:  # Only choose a new song if not paused
            print("PLAY MUSIC command...")
            file_name = random.choice(files)
            file_path = os.path.join(path_files, file_name)
            file_path = os.path.normpath(file_path)

            try:
                speak(f"Playing: {file_name}")
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
            except pygame.error as e:
                speak(f"Could not play music: {e}")
                break

        while pygame.mixer.music.get_busy() or is_paused:
            input_command = take_command()

            if not input_command:
                continue  # Ignore empty input

            if "timeout" in input_command:
                continue
            elif "change" in input_command or "skip" in input_command:
                speak("Skipping song")
                pygame.mixer.music.stop()
                is_paused = False
                break
            elif "stop music" in input_command or "stop playing music" in input_command or "stop playing" in input_command:
                pygame.mixer.quit()
                speak("Turning off the music")
                return
            elif "replay" in input_command or "rewind" in input_command or "restart" in input_command or "again" in input_command:
                speak(f"Replaying {file_name}")
                pygame.mixer.music.rewind()
                is_paused = False
            elif "pause" in input_command:
                if pygame.mixer.music.get_busy() and not is_paused:  # Check if music is playing and not already paused
                    pygame.mixer.music.pause()
                    speak("Music paused")
                    is_paused = True
            elif "resume" in input_command:
                if is_paused:  # Check if music is paused
                    pygame.mixer.music.unpause()
                    speak("Music resumed")
                    is_paused = False
            else:
                print(f"No Command Detected.")
            pygame.time.Clock().tick(10)
def timer_stopwatch(query):
    """This function is built as timer and stopwatch"""
    if "stopwatch" in query:
        start_time = time.time()
        speak("Stopwatch started")
        last_announce_time = 0

        while True:
            elapsed_time = int(time.time() - start_time)
            # Announce time passed every 10 seconds
            if elapsed_time >= last_announce_time + 10:
                last_announce_time += 10
                if last_announce_time < 60:
                    speak(f"{last_announce_time} seconds passed")
                else:
                    hours, remainder = divmod(last_announce_time, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    speak(f"{hours} hours {minutes} minutes {seconds} seconds passed")
                print(f"{last_announce_time} seconds have passed")

            # Check for stop command
            input_com = take_command()
            if "stop" in input_com:
                speak("Stopwatch stopped")
                hours, remainder = divmod(elapsed_time, 3600)
                minutes, seconds = divmod(remainder, 60)
                speak(f"Total time: {hours} hour, {minutes} minute and {seconds} second")
                return

    elif "timer" in query and any(
            unit in query for unit in ["minute", "hour", "hours", "seconds", "second", "minutes"]):
        query1 = query.replace("timer", '').replace("t-rex", '').replace("hey", '').replace("hello", '').replace(
            "stopwatch", '').replace("set", '').replace("start", "").replace("a", '').replace("for", '').replace("the",
                                                                                                                 '').replace("listen","").replace("can", '').replace("you","").replace("please","")
        query1 = query1.split()

        try:
            time1 = 0
            if "minute" in query1[-1] or "minutes" in query1[-1]:
                time1 = int(query1[-2]) * 60
            elif "second" in query1[-1] or "seconds" in query1[-1]:
                time1 = int(query1[-2])
            elif "hour" in query1[-1] or "hours" in query1[-1]:
                time1 = int(query1[-2]) * 3600

            if time1 > 0:
                speak("Timer set")
                start_time = time.time()
                d_time = int(time.time() - start_time)
                while True:
                    elapsed_time = int(time.time() - start_time)
                    if elapsed_time == d_time+1:
                       d_time=d_time +1
                       print(d_time)
                    if elapsed_time == time1 // 2:
                        speak("Half time passed")
                        print(d_time)
                        d_time = d_time + 1
                    if elapsed_time >= time1:
                        speak("TIMER ended")
                        show_alert("TIMER ended")
                        return
            else:
                speak("Timer is not set due to improper instructions")
        except Exception as e:
            print(e)
            speak("Sorry, setting a timer failed")
    else:
        speak("Unclear instructions to set timer")
def current_location(query):
    url="https://ipinfo.io"
    try:
        response=requests.get(url)
        data=json.loads(response.text)
        city=data['city']
        country=data['country']
        region=data['region']
        if country=="PK":
            country="Pakistan"
        if "city" in query:
            speak(f"YOUR CURRENT CITY IS {city}")
            return city
        elif 'region' in query or "province" in query:
            speak(f"YOUR CURRENT region IS {region}")
        elif "country" in query:
            speak(f"YOUR CURRENT country IS {country}")
        else:
            speak(f"you are in {country} your region is {region} and your current city is {city}")
    except Exception as e:
        speak("Could not tell your current location at the moment")
def weather_update(query):
    """Function for telling weather updates"""
    speak("let me check weather forecast")
    query1=query
    query1=query1.replace("weather",'').replace("about","").replace("what","").replace("is","").replace("report","").replace("give","").replace("the","").replace("temperature", '').replace("updates","").replace("update","").replace("forecast","").replace("can",'').replace("you", '').replace("please","").replace("t-rex","").replace("for","").replace("me","").replace("hey","").replace("hello","").replace("listen","").replace("condition","").replace("current","").replace("tell", '').replace("update","").replace("what's","").replace("the","").replace("right","").replace("now","").replace('will',"").replace("it","").replace("of","").replace("in","")
    query1=query1.split()
    query1=''.join(query1)  #making sure no space is left in cleared query
    print(query1)
    if query1=="":
        query1=current_location("city")
    api_key="ac5b0a4fe6ef0f31e02b00b42f0269eb"#my api_key for weather map api
    url="https://api.openweathermap.org/data/2.5/weather"
    parameters={
        'units':'metric',
        'apikey':api_key,
        'q':query1,
    }
    try:
        response=requests.get(url,params=parameters)
        weather= response.json()
        if weather['cod'] == 200:
            temperature=weather['main']['temp']
            condition=weather['weather'][0]['description']
            humidity=weather['main']['humidity']
            speed=weather['wind']['speed']
            speak(f"The weather in {query1} is {condition} with temperature of {temperature} degree celcius")
            print(f"City: {query1}")
            print(f"Temperature: {temperature} degree celcius")
            print(f"Weather Status: {condition}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {speed} m/s")
            speak("Do you want me to give detailed description?")
            input_command=take_command()
            if input_command=="timeout" or input_command=="None":
                pass
                return
            elif "yes" in input_command:
                speak(f"City: {query1}")
                speak(f"Temperature: {temperature} degree celcius")
                speak(f"Weather Status: {condition}")
                speak(f"Humidity: {humidity}%")
                speak(f"Wind Speed: {speed} m/s")
            elif 'no' in input_command:
                speak("Alright  got it")
                return
        else:
            speak(f"City {query1} not found")
    except Exception as e:
        speak("Couldn't fetch weather updates right now")

def news(query):
    '''This function is build for reading online news article from newsapi about topic asked by user.'''
    api_key = "7219d376acd244fe8230981bffcb6ee8"
    # Initialize the news client
    newsapi = NewsApiClient(api_key=api_key)
    # Clean the query
    cleaned_query = query.replace("what's", "").replace("what", "").replace('are', "").replace("regarding",
                                                                                               "").replace("t-rex",
                                                                                                           "").replace(
        "hey", '').replace("tell", "").replace("about", "").replace("the", "").replace(
        "headlines", "").replace(" in ", "").replace("world", "").replace("what's happening", "").replace("give",
                                                                                                          "").replace(
        "from", "").replace(" on ", "").replace("any", "").replace("with", '').replace("more", "").replace(
        "summary of", '').replace("to", "").replace("can", '').replace("you", "").replace('update', "").replace(
        "listen", "").replace("happened", "").replace('after', '').replace("last", "").replace("news", "").replace(
        "latest", "").replace("read","").replace(" me ", "")
    cleaned_query = cleaned_query.split()
    cleaned_query = ''.join(cleaned_query)

    # Use a default query if the cleaned query is empty
    if cleaned_query == "":
        cleaned_query = "pakistan"

    try:
        print(f"News about {cleaned_query}")

        # Set a date range for the past 7 days
        from_date = (datetime.datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        to_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # Fetch articles using the everything endpoint
        all_articles = newsapi.get_everything(q=cleaned_query, from_param=from_date, to=to_date, language='en')

        if all_articles['status'] == 'ok' and all_articles['totalResults'] > 0:
            for article in all_articles['articles']:
                speak('Article title  ')
                speak(article["title"])
                speak("Description")
                speak(article["description"])
                print("--------------------------------------------------------------------------------")
                speak("Do you want me to read another news?")
                perm = take_command()
                if "yes" in perm or "sure" in perm or "yeah" in perm or "continue" in perm:
                    speak(f"Reading another article about {cleaned_query}")
                    continue
                else:
                    speak("quiting reading news")
                    break;
        else:
            speak("No news articles found for the given query.")
    except Exception as e:
        speak(f"Sorry, could not read news at the moment. Error: {e}")
def task_manager(query):
    try:
        speak("opening task manager")
        if "clear" in query or "delete" in query or "empty" in query:
            with open('task manager',"w") as f:
                f.write("")
            speak("To do list cleared")
        elif "read" in query or "revise" in query:
            with open("task manager","r") as f:
                content=f.read()
                speak("Reading the to-do list:")
                speak(content)
        elif "add" in query or "write" in query or "update" in query:
            query1 = query.replace("add", "").replace("update ", "").replace("write ","").replace("read ", "").replace("hey ","").replace(" hi ", "").replace("hello ", "").replace("tea-rex ","").replace("tea rex ","").replace("tearex ", "").replace("dude ", "").replace("buddy ","").replace(" in ","").replace("task ","").replace("manager","").replace("schedueler","").replace("to do","").replace("to-do","").replace("list","").replace(" and ","\n").replace(" also ","\n")
            if query1=="":
                speak("what do you want to add in to-do list")
                w=take_command()
                w=w.replace("write ","").replace("hey ","").replace("hey","").replace("add ","").replace("add","").replace("sorry ","").replace("tea-rex ","").replace("oh ","").replace("yeah ","").replace(" and ","\n").replace(" also ","\n")
                if "Nothing" in w or "nothing" in w:
                    speak("Closing the task manager")
                    quit()
                else:
                    with open("task manager","a") as f:
                        f.write(w)
                        f.write("\n")
                    speak("To do list updated")
            else:
                with open("task manager", "a") as f:
                    f.write(query1)
                    f.write("\n")
                speak("To do list updated")
        else:
            print("could not get your command.")
    except Exception as e:
        speak(f"Something went wrong.Could not open task manager right now.{e}")
def send_email():
    email_list={
        "zahra":"zahrashahid916@gmail.com"
    }
    try:
        email=EmailMessage()
        speak("To whom you want to send the email?")
        name=take_command().lower()
        email["To"]=email_list[name]
        speak("what is subject of the email?")
        email["Subject"]=take_command()
        email['From']=SENDER_EMAIL
        speak("What should i say?")
        email.set_content(take_command())

        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(SENDER_EMAIL,EMAIL_PASSSWORD)
        s.send_message(email)
        s.close()
        speak("Email has been sent successfully")
    except Exception as e:
        speak(f"Could not send email right now due to some issues.")
if __name__ == "__main__":
    alarm=0
    wish_me()
    tearex_sleep = False
    while True:
        print(tearex_sleep)
        if datetime.datetime.now().strftime("%I %M %p").lower()==alarm:
            msg=f"its {datetime.datetime.now().strftime("%I %M %p").lower()}! wake up"
            speak(msg)
            alarm_alert(msg)
            alarm=0
        if not tearex_sleep:
            print("if sleep command me hon")
            query = take_command().lower()
            # speak(query)
            if "sleep" in query:
                tearex_sleep=True
                speak("sleeping")
            elif query == "timeout":
                speak("Could not recognize your command")
                continue
            elif "t-rex quit" in query or "bye t-rex" in query or "t-rex bye" in query or "bye-bye" in query or "shutdown" in query:
                speak("GoodBye")
                break
            else:
                if "stopwatch" in query or "timer" in query:
                    timer_stopwatch(query)
                elif "latest update about weather" in query or "weather" in query or "temperature" in query:
                    weather_update(query)
                elif "time" in query or "date" in query or "day" in query:
                    date_time_teller(query)
                elif "hello" in query or "hello t-tex" in query or "hey" in query or "hey t-rex" in query:
                    speak("hii\n how are you?")
                elif "how are you" in query or "t-rex how are you" in query:
                    speak("i am fine\n what about you")
                elif "i am fine" in query or "i am good" in query or "i am okay" in query:
                    speak("That's great")
                elif "thanks" in query or "thank you" in query or "thankyou" in query:
                    speak("you are welcome!")
                elif "are you dumb" in query or "dumbo" in query:
                    speak("sorry if i caused any trouble\nbut don't you think calling me dumb is unfair")
                elif "you are wrong" in query or "incorrect" in query or "wrong" in query or "i was correct" in query:
                    speak("I am pretty sorry if i cause any inconvenience.I will be more careful next time")
                elif "who are you" in query or "Introduce yourself " in query or "your introduction" in query or query == "tell me about yourself" or "your name" in query:
                    tea_rex()
                elif "t-rex are your there" in query or "t-rex are you listening" in query or "t-rex" in query or "t rex" in query:
                    speak("yes i am listening")
                elif "your religion" in query or "are you muslim" in query:
                    speak("WELL  I am a virtual assistant so i don't have any religion \nBut in my view point islam is best religion to follow")
                elif "your age" in query or "how old are you" in query:
                    tea_rex_age_calculation()
                elif "who created you" in query or "who is your owner" in query:
                    speak("I was created by Zahra Shahid on 18th June 2024")
                elif 'live location' in query or "current location" in query or "location" in query or "city" in query or "country" in query or "region" in query or "province" in query:
                    current_location(query)
                elif "news" in query or "latest update" in query or "updates" in query or "latest updates" in query or "headlines" in query or "what's happening in world" in query:
                    news(query)
                elif "wikipedia" in query or "information" in query or "tell me about" in query:
                    wiki(query)
                elif "open word" in query:
                    path = "C:/Program Files\\Microsoft Office/root/Office16/WINWORD.EXE"
                    speak("opening microsoft word")
                    os.startfile(path)
                elif "open excel" in query:
                    path= "C:/Program Files\\Microsoft Office/root/Office16/EXCEL.EXE"
                    speak("opening microsoft Excel")
                    os.startfile(path)
                elif "open powerpoint" in query:
                    path= "C:/Program Files\\Microsoft Office/root/Office16/POWERPNT.EXE"
                    speak("opening microsoft powerpoint")
                    os.startfile(path)
                elif "open chrome" in query:
                    path = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
                    speak("opening chrome")
                    os.startfile(path)
                elif "open" in query:
                    opening_websites(query)
                elif "search" in query:
                    if "youtube" in query:
                        search_youtube(query)
                    if "google" in query:
                        search_google(query)
                elif "set alarm" in query or "set reminder" in query or "remind me" in query or "set an alarm" in query or "alarm" in query:
                    alarm=reminder_alarm(query)
                elif "play music" in query:
                    play_music()
                elif "task manager" in query or "to do" in query or "read the list" in query or "write in list" in query or "to-do list" in query or "to-do" in query or "tasks" in query or "task" in query:
                    task_manager(query)
                elif "send email" in query:
                    send_email()
                else:
                    speak(f"you said {query}")
        else:
            input=take_command()
            if "wake up" in input or "wake-up" in input or "wakeup" in input:
                tearex_sleep=False
                speak("i'm awaked")