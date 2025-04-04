# Bluevoice-
Voice assistant for macOS that can open apps, control volume, scan/connect Bluetooth devices — all with your voice.

🔊 BlueVoice - Voice-Controlled Mac Automation with Bluetooth
BlueVoice is a Python-based voice assistant that allows you to control your macOS system through voice commands. You can open apps, adjust volume, lock the screen, and even scan/connect Bluetooth devices — all hands-free!

🚀 Features
🎙️ Voice command recognition using Google Speech API

🔊 Text-to-speech responses with pyttsx3

🧠 Smart background noise handling

🔒 Lock and unlock system with voice

📡 Scan and connect to Bluetooth devices

📁 Open common apps like Chrome, TextEdit etc.

🔇 Volume control using voice

🔌 System shutdown command

🧰 Technologies Used
Python 3.13+

SpeechRecognition

PyAudio

pyttsx3

pyautogui

bleak (for Bluetooth access)

asyncio

🖥️ System Requirements
macOS system

Python 3.13+

Microphone access

Admin access (for shutdown command)

Bluetooth enabled

⚙️ Installation
bash
Copy
Edit
# Clone the repo
git clone https://github.com/Deependra7747/bluevoice.git
cd bluevoice

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
▶️ How to Run
bash
Copy
Edit
python3 voice_control.py
Say:

"open chrome"

"lock laptop"

"volume up"

"scan bluetooth"

"connect bluetooth <device name>"

"shutdown"

📌 Note
Make sure your microphone is working and not muted.

For shutdown, macOS will ask for admin password.

App names must match the system’s default names (e.g., "TextEdit" not "Notepad" on Mac).


