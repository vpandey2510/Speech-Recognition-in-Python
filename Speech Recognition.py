#Before start coding the program remember to INSTALL ALL the required modules/packages in the project
#Go in terminal and install following used packages of python
#Tkinter for all GUI
#Google Speech API for conversion
#Speech Recognition
#PyAudio for microphone

#importing different modules in the program

from tkinter import *           #pip install tk
import tkinter.font as font         #using fonts available in Tkinter as font
import speech_recognition as sr       #pip install SpeechRecognition
import time       

#Creating GUI for display and interaction between user and interface
#configuration of window panels could be change by giving different values

root = Tk()         #Creating a window panel
root.title("Python Project")      #Giving title to the panel
root.configure(bg="light blue")       #setting background color of panel
root.geometry("800x600")        #setting width and height of panel
label1 = Label(root, text = "Speech Recognition Program using Python", bg = "Black", fg = "White")        #labelling the window
label1.config(font=("exotc350 bd bt", 40))
label1.pack(pady=10)

newFont = font.Font(family="EngraversGothic BT", size=25, weight="bold")        #declaring a font family for further use all over the program at once

print("Welcome to Speech Recognition Program")

label2 = Label(root)

#This section is for recognizing the audio -> Processing it with Google Speech API -> Converting it into text

def speech2txt():
    r = sr.Recognizer()       #recogninzing instance

    with sr.Microphone() as source:
        #setting microphone as input device
        print("Try saying something!")
        audio = r.listen(source)        #listening to the audio

        try:
            msg = r.recognize_google(audio)       #recognizing the audio and converting into text
            print("You said:", msg)
            label2['text'] = msg
            label2.config(font=("impact", 20), bg="black", fg="white")
            label2.pack(pady=40)

                 #label will display the text gained from audio

        except:
            #if the program was unable to recognize the instance

            print("SORRY, not able to recognize!")
            label2['text']="SORRY, not able to recognize!"
            label2.config(font=("impact", 20), bg="red", fg="black")
            label2.pack(pady=40)
                #if audio is not recognized by API

#Closing of program when user wants

def close():
    print("Closing program...")
    exit()        #to close the program

#Button used in the program for interaction   

b1 = Button(root, text = "Tap to Speak", padx=5, pady=10, bg="green", fg="black", command=speech2txt)
b1['font'] =  newFont
b1.pack(padx=20, pady=10)
#button to start speaking
b2 = Button(root, text = "EXIT", padx=5, pady=10, bg="red", fg="black", command=close)
b2['font'] =  newFont
b2.pack(padx=10)
      #button for exiting the program

root.mainloop()       #main event loop
