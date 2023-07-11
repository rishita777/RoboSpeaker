import win32com.client as wincom
if __name__ == '__main__':
    print("---------------------Welcome to robo speaker-----------------------")
    print("-------to stop write Stop------")
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        x = input("enter what u want to speak : ")
        if x == "stop":
            break
        speak.Speak({x})

