import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import pyautogui
import os
import asyncio

try:
    from bleak import BleakScanner, BleakClient
    BLEAK_AVAILABLE = True
except ImportError:
    BLEAK_AVAILABLE = False

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            return recognizer.recognize_google(audio).lower()
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            return ""

def scan_bluetooth_devices():
    if not BLEAK_AVAILABLE:
        speak("Bluetooth functionality is not available.")
        return []

    print("Scanning for Bluetooth devices...")
    devices = []

    async def scan():
        found_devices = await BleakScanner.discover()
        for device in found_devices:
            if device.name:
                print(f"Found {device.name} at {device.address}")
                devices.append((device.address, device.name))

    try:
        asyncio.run(scan())
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(scan())

    return devices

def connect_bluetooth_device(target_name):
    if not BLEAK_AVAILABLE:
        speak("Bluetooth module not available.")
        return False

    devices = scan_bluetooth_devices()
    for addr, name in devices:
        if name and target_name.lower() in name.lower():
            print(f"Connecting to {name} ({addr})...")
            return True
    print("Device not found.")
    return False

def access_bluetooth_data(target_address):
    if not BLEAK_AVAILABLE:
        speak("Bluetooth data access not available.")
        return

    async def read_data():
        async with BleakClient(target_address) as client:
            if client.is_connected:
                print(f"Connected to {target_address}")
                services = await client.get_services()
                for service in services:
                    print(f"Service: {service.uuid}")
                    for char in service.characteristics:
                        print(f"Characteristic: {char.uuid}")

    try:
        asyncio.run(read_data())
    except Exception as e:
        print(f"Failed to read data: {e}")

def execute_command(command):
    command = command.lower()

    if "chrome" in command:
        speak("Opening Chrome")
        os.system("open -a 'Google Chrome'")
    elif "notepad" in command or "text editor" in command:
        speak("Opening TextEdit")
        os.system("open -a 'TextEdit'")
    elif "finder" in command or "file manager" in command:
        speak("Opening Finder")
        os.system("open -a 'Finder'")
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("open -a 'Calculator'")
    elif "vlc" in command:
        speak("Opening VLC Player")
        os.system("open -a 'VLC'")
    elif "close window" in command:
        speak("Closing window")
        pyautogui.hotkey("command", "w")
    elif "volume up" in command:
        speak("Increasing volume")
        pyautogui.press("volumeup", presses=5)
    elif "volume down" in command:
        speak("Decreasing volume")
        pyautogui.press("volumedown", presses=5)
    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("sudo shutdown -h now")
    elif "lock laptop" in command:
        speak("Locking laptop")
        os.system("pmset displaysleepnow")
    elif "unlock laptop" in command:
        speak("Unlocking laptop")
        print("Unlocking process initiated")
    elif "scan bluetooth" in command:
        speak("Scanning Bluetooth devices")
        scan_bluetooth_devices()
    elif "connect bluetooth" in command:
        speak("Trying to connect Bluetooth device")
        target_device = command.replace("connect bluetooth", "").strip()
        connect_bluetooth_device(target_device)
    elif "access bluetooth data" in command:
        speak("Accessing Bluetooth data")
        target_address = command.replace("access bluetooth data", "").strip()
        access_bluetooth_data(target_address)
    else:
        print("Command not recognized.")
        speak("I did not understand that command.")

if __name__ == "__main__":
    speak("Voice control system activated. How can I help you Deependra?")
    while True:
        user_command = recognize_speech()
        if user_command:
            if "exit" in user_command or "stop" in user_command:
                speak("Shutting down voice control.")
                break
            execute_command(user_command)