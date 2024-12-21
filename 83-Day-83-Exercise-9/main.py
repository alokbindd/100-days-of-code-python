import win32com.client 

speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Alok Bind","Amit Bind","Ankit Bind","Dhiraj Kewat"]

for i in l:
    speaker.Speak("shout out to "+i)
    print("shout out to "+i)

speaker.Speak("Thank you for listening")