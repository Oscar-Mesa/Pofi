import speech_recognition as sr
import spacy

nlp_ner = spacy.load('NER/version1/model-best')

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Di algo...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language="es-COL")
            print("Has dicho:", text)
            break  # Salir del bucle si se reconoce el texto correctamente
    except sr.UnknownValueError:
        print("No se pudo entender el audio. Vuelve a intentarlo.")
    except sr.RequestError:
        print("Error en la solicitud. Vuelve a intentarlo.")

# Continuar con el código después de reconocer el texto correctamente
print("Continuación del programa...")




doc = nlp_ner(str(text))


spacy.displacy.render(doc, style="ent", jupyter=True)
