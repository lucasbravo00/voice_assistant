import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'


# Listen to microphone and return audio as text
def convert_audio_to_text(audio_path):
    # Store recognizer in a variable
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # Inform good functionality
        r.pause_threshold = 0.8

        # Save what is heard as audio
        audio = r.listen(source)

        try:
            # Search using Google
            command = r.recognize_google(audio, language='en-US')

            # Test
            print('You said: ' + command)

            # Return command
            return command

        # Did not understand the audio
        except sr.UnknownValueError:
            print("I didn't understand")
            return "I'm still waiting"

        # Could not process the request
        except sr.RequestError:
            print("I can't process it")
            return "I'm still waiting"

        # Unexpected error
        except:
            print("An error occurred")
            return "I'm still waiting"


# Function to make the assistant speak
def speak(message):
    # Activate pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Pronounce message
    engine.say(message)
    engine.runAndWait()


# Inform the day of the week
def get_day():
    # Create a variable with today's data
    today = datetime.date.today()
    weekday = today.weekday()

    # Dictionary with day names
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # Say the day of the week
    speak(f'Today is: {calendar[weekday]}')


# Inform the current time
def get_time():
    # Time variable
    current_time = datetime.datetime.now()
    current_time = f'Right now it is {current_time.hour} hours, {current_time.minute} minutes, and {current_time.second} seconds'

    # Say the time
    speak(current_time)


# Initial greeting function
def initial_greeting():
    # Variable with current hour data
    hour = datetime.datetime.now()
    if hour.hour >= 20 or hour.hour < 6:
        moment = 'Good evening'
    elif 6 <= hour.hour < 13:
        moment = 'Good morning'
    else:
        moment = 'Good afternoon'

    # Greet
    speak(f'{moment}, I am Elena, your personal assistant. Please tell me how I can help you')


# Main function of the assistant
def assistant_main_function():
    # Activate initial greeting
    initial_greeting()

    # Assistant execution
    start = True
    while start:

        # Activate microphone and save command as string
        command = convert_audio_to_text().lower()

        if 'open youtube' in command:
            speak('Sure, opening YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in command:
            speak('Of course, I am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in command:
            get_day()
            continue
        elif 'what time is it' in command:
            get_time()
            continue
        elif 'search on wikipedia' in command:
            speak('Perfect, I am searching on Wikipedia')
            command = command.replace('search on wikipedia', '')
            wikipedia.set_lang('en')
            result = wikipedia.summary(command, sentences=1)
            speak(result)
            continue
        elif 'search the internet' in command:
            speak('I am searching now')
            command = command.replace('search the internet', '')
            pywhatkit.search(command)
            speak('Here is what I found')
            continue
        elif 'play' in command:
            speak('Great idea, I will play it now')
            pywhatkit.playonyt(command)
            continue
        elif 'tell me a joke' in command:
            speak(pyjokes.get_joke('en'))
            continue
        elif 'stock price of' in command:
            stock = command.split('of')[-1].strip()
            portfolio = {'apple': 'AAPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'}
            try:
                searched_stock = portfolio[stock]
                searched_stock = yf.Ticker(searched_stock)
                current_price = searched_stock.info['regularMarketPrice']
                speak(f'I found it, the price of {stock} is {current_price}')
                continue
            except:
                speak("Sorry, I couldn't find it")
        elif 'goodbye' in command:
            speak('Goodbye, I am going to rest, let me know if you need anything')
            break


assistant_main_function()
