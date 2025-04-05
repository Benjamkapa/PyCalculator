import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_input():
    # Use the microphone to listen for the operation and numbers
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()  # Use Google API to recognize speech
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Please try again.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech service. Please try again later.")
        return ""

def calculate(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                result = "Error: Division by zero"
                speak(result)
                result_label.config(text=f"Result: {result}")
                return
            else:
                result = a / b
        elif op == '%':
            result = a % b
        elif op == '^':
            result = a ** b
        else:
            result = "Invalid Operation"

        result_text = f"Result: {result}"
        result_label.config(text=result_text)
        speak(result_text)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
        speak("Invalid input. Please enter valid numbers.")

def get_input_from_voice():
    speak("Please say the first number.")
    num1_str = listen_for_input()
    entry1.delete(0, tk.END)
    entry1.insert(0, num1_str)

    speak("Please say the second number.")
    num2_str = listen_for_input()
    entry2.delete(0, tk.END)
    entry2.insert(0, num2_str)

# GUI setup
root = tk.Tk()
root.title("Benja's Talking Calculator")
root.geometry("300x400")

# Entry Fields for Numbers
entry1 = tk.Entry(root, width=15)
entry1.pack(pady=10)

entry2 = tk.Entry(root, width=15)
entry2.pack(pady=10)

# Button for Voice Input
voice_input_button = tk.Button(root, text="Use Voice Input", command=get_input_from_voice)
voice_input_button.pack(pady=10)

# Buttons for operations
for symbol in ['+', '-', '*', '/', '%', '^']:
    btn = tk.Button(root, text=symbol, width=10, command=lambda op=symbol: calculate(op))
    btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=20)

root.mainloop()
