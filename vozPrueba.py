import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)
    #text = r.recognize_google(audio, language="es")
    text = r.recognize_google(audio, language="es")

    print("Has dicho:", text)



