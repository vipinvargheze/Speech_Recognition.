import speech_recognition as sr
import wikipedia
def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        data = r.recognize_google(audio)
        print(data)
audio()