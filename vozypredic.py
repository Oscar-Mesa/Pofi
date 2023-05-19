import spacy
import speech_recognition as sr

nlp_ner = spacy.load('NER/version3/model-best')
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)
    
try:
    text = r.recognize_google(audio, language="es-COL")
    print("Has dicho:", text)
    
    doc = nlp_ner(str(text))
    
    for ent in doc.ents:
        print(ent.text, ent.label_)

except sr.UnknownValueError:
    print("No se pudo entender el audio. Vuelve a intentarlo.")
except sr.RequestError:
    print("Error en la solicitud. Vuelve a intentarlo.")
