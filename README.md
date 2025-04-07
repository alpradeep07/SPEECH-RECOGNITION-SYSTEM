NAME : AAKINA LAKSHMI PRADEEP

COMPANY : CODTECH IT SOLUTIONS

INTERN ID : CT06WR44

DOMAIN : EMBEDDED SYSTEMS

DURATION : MARCH 30th, 2025 to MAY 15th, 2025 (6 WEEKS)

MENTOR : NEELA SANTHOSH

OVERVIEW : SPEECH RECOGNITION SYSTEM


### **System Design for a Speech Recognition System to Control Devices Using an Embedded Board**

In this section, we will design a **basic speech recognition system** that can control devices based on voice commands, using an embedded board (like the **Raspberry Pi**). This system will listen for voice commands, process the audio, and perform specific actions like turning devices (LEDs, motors, etc.) on or off.

#### **Key Components**

1. **Hardware Components:**
   - **Embedded Board**: Raspberry Pi 3 or 4 (or any embedded system with GPIO pins and microphone support).
   - **Microphone**: USB microphone or an external microphone module to capture audio input.
   - **Devices to Control**: Example devices like **LEDs**, **motors**, or other IoT devices connected to the Raspberry Pi GPIO pins.
   - **Speakers (Optional)**: For providing audio feedback (if you want the system to give voice responses).

2. **Software Components:**
   - **Raspbian OS**: The operating system for Raspberry Pi.
   - **Python**: For scripting the control logic.
   - **SpeechRecognition Library**: For processing speech inputs.
   - **GPIO Library**: For controlling GPIO pins on the Raspberry Pi.
   - **PyAudio**: To capture real-time audio from the microphone.
   - **Optional Libraries**: For adding text-to-speech (TTS) feedback (e.g., pyttsx3 for audio responses).

---

### **System Architecture**

1. **Microphone Input:**
   - The microphone is used to capture the voice command from the user. This is input into the Raspberry Pi.
   - The microphone sends an audio signal to the Raspberry Pi, which will be processed by the Speech Recognition system.

2. **Speech Recognition Process:**
   - The captured audio is processed using the **SpeechRecognition library** to convert the speech into text.
   - This text is then compared with predefined commands to understand the intent of the user.

3. **Device Control:**
   - Based on the recognized command, the system will activate or deactivate devices connected to the Raspberry Pi's GPIO pins.
   - For example, a command like "turn on the light" will turn on an LED, and "turn off the light" will turn it off.

4. **Audio Feedback (Optional):**
   - If you want the system to speak back to the user (e.g., "LED turned on"), you can use a Text-to-Speech library like **pyttsx3** to provide audio responses.

---

### **Detailed System Design**

#### **1. Hardware Setup**

1. **Raspberry Pi:**
   - Install **Raspbian OS** on the Raspberry Pi.
   - Ensure it has internet access to download required libraries.
   
2. **Microphone:**
   - Plug a **USB microphone** into the Raspberry Pi.
   - Check microphone functionality:
     ```bash
     arecord -l
     ```
   - This will list the available audio input devices.

3. **Devices to Control:**
   - **LED Control Example**: Connect an LED to a GPIO pin (e.g., GPIO 17) using a current-limiting resistor.
   - You can control other devices like motors, fans, or relays connected to the Raspberry Pi GPIO pins.

---

#### **2. Software Setup**

1. **Install Dependencies:**
   - On the Raspberry Pi, install the necessary libraries:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-pyaudio python3-speechrecognition python3-gpiozero python3-pyttsx3
     ```

2. **Python Script for Speech Recognition and Device Control:**

   **Speech Recognition Workflow:**
   - The Python script will listen to commands via the microphone.
   - The system will recognize speech and control devices based on the command (e.g., turning on/off an LED).

   **Python Code Example**:

   ```python
   import speech_recognition as sr
   import RPi.GPIO as GPIO
   import pyttsx3
   from time import sleep

   # Setup GPIO for controlling devices
   GPIO.setmode(GPIO.BCM)
   LED_PIN = 17  # GPIO pin for LED
   GPIO.setup(LED_PIN, GPIO.OUT)

   # Initialize text-to-speech engine
   engine = pyttsx3.init()

   # Function to speak feedback
   def speak(text):
       engine.say(text)
       engine.runAndWait()

   # Function to control devices based on voice command
   def control_device(command):
       if "turn on" in command:
           GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
           speak("LED turned on")
       elif "turn off" in command:
           GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
           speak("LED turned off")
       else:
           speak("Command not recognized")

   # Initialize recognizer
   recognizer = sr.Recognizer()

   # Main loop for listening to voice commands
   while True:
       with sr.Microphone() as source:
           print("Listening for commands...")
           recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
           audio = recognizer.listen(source)  # Listen for speech

       try:
           print("Recognizing speech...")
           command = recognizer.recognize_google(audio)  # Recognize using Google Speech API
           print(f"Command received: {command}")
           control_device(command.lower())  # Process the command
       except sr.UnknownValueError:
           print("Sorry, I did not understand the command.")
       except sr.RequestError:
           print("Error with the speech recognition service.")

       sleep(1)  # Add a small delay to avoid continuous listening
   ```

#### **Code Explanation**:

- **Speech Recognition**: The script uses the **SpeechRecognition** library to capture audio from the microphone and convert it to text.
- **GPIO Control**: The script uses the **RPi.GPIO** library to control the LED. Based on the recognized command (like "turn on"), the corresponding action is taken.
- **Text-to-Speech**: The **pyttsx3** library is used for providing feedback to the user (e.g., "LED turned on").
- **Main Loop**: The system continuously listens for commands and processes them.

---

### **3. Testing the System**

1. **Run the Script**:  
   Save the script to your Raspberry Pi (e.g., `speech_control.py`) and run it using:
   ```bash
   python3 speech_control.py
   ```

2. **Give Commands**:
   - Say **"turn on"** and the LED connected to GPIO 17 should light up.
   - Say **"turn off"** and the LED should turn off.

3. **Check Feedback**:  
   If you’ve enabled voice feedback, the system will speak the actions it has performed (e.g., "LED turned on").

---

### **4. Optional Enhancements**

- **Add More Devices**:  
   You can add more devices to the Raspberry Pi, such as motors or relays. Add additional GPIO control logic in the `control_device()` function.

- **Offline Speech Recognition**:  
   To make the system work offline, you can use libraries like **pocketsphinx** instead of Google’s cloud API.

- **Voice Authentication**:  
   For security, you could implement voice authentication by using a voice recognition library to identify specific users before accepting commands.

- **Multi-command Processing**:  
   Enhance the system to recognize a list of commands such as controlling multiple lights, fan speed, etc.

---

### **Conclusion**

This system design provides a complete approach to building a **speech recognition-based device control system** using an embedded board like the **Raspberry Pi**. The system listens for voice commands, processes them, and controls devices such as LEDs based on the recognized command. You can expand this project by adding more devices, improving command recognition, or adding additional features such as voice feedback.
