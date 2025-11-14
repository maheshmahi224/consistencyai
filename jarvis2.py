import os
import requests
import pyttsx3
import speech_recognition as sr
from deep_translator import GoogleTranslator

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set your OpenRouter API key
OPENROUTER_API_KEY = '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'  # Replace with your valid key

def speak(text, lang='en'):
    translated = GoogleTranslator(source='auto', target=lang).translate(text)
    engine.say(translated)
    engine.runAndWait()

def listen_command(timeout=10, phrase_time_limit=30):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Optional: reduce background noise
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            query = r.recognize_google(audio)
            print("🗣️ You said:", query)
            return query
        except sr.UnknownValueError:
            print("⚠️ MALLI CHEPPU ARDHAM KALE.")
            return ""
        except sr.RequestError:
            print("⚠️ NA VALLE KALE MALLI TRY CHEY.")
            return ""

def get_openrouter_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Use another model if needed
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant. Keep responses under 4 sentences."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        if 'choices' in result:
            return result['choices'][0]['message']['content'].strip()
        elif 'error' in result:
            return f"OpenRouter Error: {result['error']['message']}"
        else:
            return "❌ No valid response from server."
    except Exception as e:
        return f"Exception: {str(e)}"

def execute_command(command):
    cmd = command.lower()
    if "open notepad" in cmd:
        os.system("notepad.exe")
        return "Opening Notepad"
    elif "open chrome" in cmd:
        os.system("start chrome")
        return "Opening Chrome"
    elif "shutdown" in cmd:
        os.system("shutdown /s /t 1")
        return "Shutting down the system"
    elif "restart" in cmd:
        os.system("shutdown /r /t 1")
        return "Restarting the system"
    else:
        return get_openrouter_response(command)

# Main execution
if __name__ == "__main__":
    speak("Hello mahesh , I am your jarvis. Which language should I speak i prefer english?", 'en')
    lang = listen_command().lower()

    # Language map
    lang_map = {
        "english": "en",
        "hindi": "hi",
        "chinese": "zh-cn",
        "russian": "ru",
        "japanese": "ja",
        "spanish": "es"
    }
    lang_code = lang_map.get(lang, "en")
    speak("Say something you want me to do", lang_code)

    while True:
        command = listen_command(timeout=10, phrase_time_limit=20)
        if command:
            result = execute_command(command)
            print("🤖 Jarvis:", result)
            speak(result, lang_code)
        if "exit" in command.lower() or "stop" in command.lower():
            speak("Goodbye!", lang_code)
            break
