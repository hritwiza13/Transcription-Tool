import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen and respond
def listen_and_respond():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for speech...")
        audio = recognizer.listen(source)
    
    # Recognize speech
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Respond with TTS
        speak("You said: " + text)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the speech.")
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Could not connect to the recognition service.")
        speak("I am having trouble connecting to the recognition service.")

# Run the function
listen_and_respond()
