import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# Setup GPIO mode and pins (e.g., pin 18 for the light control)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Assuming pin 18 controls a device (e.g., a light)

# Initialize recognizer
recognizer = sr.Recognizer()

# Define function to turn on and off a device
def control_device(command):
    if "on" in command:
        GPIO.output(18, GPIO.HIGH)  # Turn on the device
        print("Device is ON")
    elif "off" in command:
        GPIO.output(18, GPIO.LOW)  # Turn off the device
        print("Device is OFF")
    else:
        print("Unknown command")

# Capture audio and recognize commands
while True:
    with sr.Microphone() as source:
        print("Please say a command (e.g., 'turn on' or 'turn off'):")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)
            control_device(command)  # Control the device based on the command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the Google Speech API: {e}")

    # Delay to avoid continuous listening
    time.sleep(1)
