import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser


recognizer = sr.Recognizer()


engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")  
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5) 
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio.")
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, my speech service is down.")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            speak("Listening timed out.")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An error occurred.")
            return ""

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    return response.url

def main():
    speak("Hello Raunak, I am your personal assistant ronnie,how can I help you today?")
    
    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hi there!")
            elif "time" in command:
                current_time = get_time()
                speak(f"The current time is {current_time}")
            elif "date" in command:
                current_date = get_date()
                speak(f"Today's date is {current_date}")
            elif "search" in command:
                speak("What do you want to search for?")
                query = listen()
                if query:
                    search_url = search_web(query)
                    speak(f"Here is what I found for {query}: {search_url}")
            elif "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif "open poki" in command:
                speak("Opening Poki")
                webbrowser.open("https://www.poki.com")
            elif "open wikipedia" in command:
                speak("Opening Wikipedia")
                webbrowser.open("https://www.wikipedia.org")
            elif "stop" in command or "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't catch that. Please try again.")
        else:
            print("No valid command received, listening again.")

if __name__ == "__main__":
    main()
