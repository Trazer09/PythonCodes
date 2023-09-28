import pyttsx3

if __name__ == '__main__':
    print("Welcome to ROBO")
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want to speak (or 'q' to quit): ")
        if x == "q":
            engine.say("Bye Bye")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
