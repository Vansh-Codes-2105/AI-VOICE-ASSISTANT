from enum import Flag
import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(f"Available voices: {voices}")
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 7, 5)

        try:
            print('Recognizing...')
            eel.DisplayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            eel.DisplayMessage(query)
            time.sleep(2)
        except Exception as e:
            print(f"Error in recognition: {e}")  # Debugging
            return ""

        return query.lower()

@eel.expose
def allCommands(message=1):
    print(f"Received message: {message}")  # Debugging

    if message == 1:
        query = takecommand()
        print(f"Processed command: {query}")
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, sendMessage, makeCall
            contact_no, name = findContact(query)

            if contact_no != 0:
                speak("Which mode do you want to use, WhatsApp or Mobile?")
                preference = takecommand().lower()
                print(f"User Preference: {preference}")

                if "mobile" in preference:
                    if "send message" in query or "send sms" in query:
                        speak("What message should I send?")
                        message = takecommand()
                        
                        if message.strip():
                            sendMessage(message, contact_no, name)  
                        else:
                            speak("Message cannot be empty.")
                        
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    
                    else:
                        speak("Please try again.")

                    return  # Exit to prevent further execution of WhatsApp logic
                
                if contact_no != 0:
                    flag = ""
                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                elif "phone call" in query:
                    flag = 'voice call'
                else:
                    flag = 'video call'
                whatsApp(contact_no, query, flag, name)  

        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print(f"Error in command execution: {e}")

    eel.ShowHood()