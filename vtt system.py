import speech_recognition as sr
import keyboard

def listen_and_convert():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak... ")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=10)
            print("Record Start")

            text = recognizer.recognize_google(audio, language="ms-MY")
            print("You said:", text)

            with open ("output.txt", "a", encoding="utf-8") as f:
                f.write(text + "\n")

        except sr.UnknowValueError:
            print("Not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request result from service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("press 's' to start listening")
    while True:
        if keyboard.is_pressed ('s'):
            listen_and_convert()
        elif keyboard.is_pressed ('q'):
            print("Stop Record...")
            break