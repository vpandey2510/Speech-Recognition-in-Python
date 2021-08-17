from tkinter import *
import tkinter.font as font
import speech_recognition as sr
import time

root = Tk()#Creating a window panel
root.title("Python project")#Giving title to the panel
root.configure(bg="light blue")#setting background color of panel
root.geometry("800x600")#setting width and height of panel
label1 = Label(root, text = "Speech Recognition Program using Tkinter", bg = "Black", fg = "White")
label1.config(font=("exotc350 bd bt", 40))
label1.pack(pady=10)

newFont = font.Font(family="EngraversGothic BT", size=25, weight="bold")#declaring a font family for further use.

print("Welcome to Speech Recognition Program")

label2 = Label(root)


def speech2txt():
    r = sr.Recognizer()#recogninzing instance

    with sr.Microphone() as source:
        #setting microphone as input device
        print("Try saying something!")
        audio = r.listen(source)#listening to the audio
        
        try:
            msg = r.recognize_google(audio)#recognizing the audio and converting into text
            print("You said:", msg)
            label2['text'] = msg
            label2.config(font=("impact", 20), bg="black", fg="white")
            label2.pack(pady=40)
            #label will display the text gained from audio
            
        except:
            print("SORRY, not able to recognize!")
            label2['text']="SORRY, not able to recognize!"
            label2.config(font=("impact", 20), bg="red", fg="black")
            label2.pack(pady=40)
            #if audio is not recognized by API

def close():
    print("Closing program...")
    exit()#to close the program
    
b1 = Button(root, text = "Tap to Speak", padx=5, pady=10, bg="green", fg="black", command=speech2txt)
b1['font'] =  newFont
b1.pack(padx=20, pady=10)
#button to start speaking
b2 = Button(root, text = "EXIT", padx=5, pady=10, bg="red", fg="black", command=close)
b2['font'] =  newFont
b2.pack(padx=10)
#button for exiting the program

root.mainloop()#main event loop
