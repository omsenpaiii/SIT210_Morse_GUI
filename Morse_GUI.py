import RPi.GPIO as GPIO
import time
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x150")
window.title("Blink Your Name in Morse")

# Create a frame to hold widgets
frame = Frame(window)
frame.pack(pady=20, padx=20)

# Add a heading label with colorful text
heading_label = Label(frame, text="Blink Your Name in Morse", font=("Helvetica", 16), fg="blue")
heading_label.pack()

# Input text box with a colorful border
textInput = StringVar()
textEntry = Entry(frame, width=12, textvariable=textInput, font=("Helvetica", 12))
textEntry.pack(pady=10)
textEntry.configure(highlightbackground="green", highlightcolor="green")

# Convert button with a colorful background
def convertToCode():
    MorseText = textInput.get().upper()
    if len(MorseText) > 12:
        return
    for char in MorseText:
        if char == ' ':
            time.sleep(unit * 6)  # 7 units for space between words
        elif char in morse_code:
            code = morse_code[char]
            for symbol in code:
                if symbol == '.':
                    dot()
                elif symbol == '-':
                    dash()
                time.sleep(unit)
            newChar()

convertButton = Button(frame, text="Convert to Morse Code", command=convertToCode, bg="orange", fg="white", font=("Helvetica", 12))
convertButton.pack()

# Function to change button color on hover
def on_enter(e):
    convertButton.configure(bg="red")

def on_leave(e):
    convertButton.configure(bg="orange")

# Bind events to button
convertButton.bind("<Enter>", on_enter)
convertButton.bind("<Leave>", on_leave)

# Setup GPIO
LED = 18  # LED pin number
unit = 0.5  # sets the unit length for the morse code

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

# Morse code functions
def dot():
    GPIO.output(LED, True)
    time.sleep(unit)
    GPIO.output(LED, False)
    time.sleep(unit)

def dash():
    GPIO.output(LED, True)
    time.sleep(unit * 3)
    GPIO.output(LED, False)
    time.sleep(unit)

def newChar():
    time.sleep(unit * 2)

window.mainloop()