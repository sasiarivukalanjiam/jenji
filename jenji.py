
# pip install pyttsx3
# pip install SpeechRecognition
# pip install PyAudio
# pip install pypiwin32

import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print("Driver is not found")
except RuntimeError:
    print("Driver fails to initialize")

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)

engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0")
rate = engine.getProperty("rate")
engine.setProperty("rate",rate)

def speak_test_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print("!! listening ...!!")
    with sr.Microphone() as source:
        audio = speech.listen(source)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Network Error")
    return voice_text

if __name__ == '__main__':
    speak_test_cmd("Hello Sasi. This is Jenji your Artificial Inteligence")
    while True:
        voice_note = read_voice_cmd()
        print("cmd : {}".format(voice_note))
        if "hello" in voice_note:
            speak_test_cmd("Hello Sasi, How can i help you?")
            continue
        elif "open" in voice_note:
            os.system('explorer c:\\ {}'.format(voice_note.replace('Open ','')))
            continue
        elif "bye" in voice_note:
            speak_test_cmd("Good Bye Sasi !! ")
            exit()


