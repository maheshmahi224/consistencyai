import os
import requests
import pyttsx3
import speech_recognition as sr
from deep_translator import GoogleTranslator

# 🔑 Your OpenRouter (Mistral-supported) API key
OPENROUTER_API_KEY = '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'

# 🗣️ Text-to-speech engine
engine = pyttsx3.init()

# 🔊 Speak out loud with language translation
def speak(text, lang='en'):
    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
    except Exception:
        translated = text
    engine.say(translated)
    engine.runAndWait()

# 🎧 Listen to microphone input
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            audio = r.listen(source, timeout=5)
            query = r.recognize_google(audio)
            print("🗣️ You said:", query)
            return query
        except sr.WaitTimeoutError:
            print("⚠️ Timeout: No input")
        except sr.UnknownValueError:
            print("⚠️ Could not understand")
        except sr.RequestError as e:
            print(f"⚠️ Speech recognition error: {e}")
        return ""

# 🧠 Get response from Mistral via OpenRouter
def get_openrouter_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # ✅ Using Mistral model
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant. Keep your answers short and to the point, in 2-4 sentences max."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        if 'choices' in result:
            return result['choices'][0]['message']['content'].strip()
        elif 'error' in result:
            return f"OpenRouter Error: {result['error']['message']}"
        else:
            return "❌ No response from OpenRouter."
    except Exception as e:
        return f"Exception: {str(e)}"

# ⚙️ Handle system commands
def execute_command(command):
    command = command.lower()
    if "open notepad" in command:
        os.system("notepad.exe")
        return "Opening Notepad"
    elif "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the system"
    elif "restart" in command:
        os.system("shutdown /r /t 1")
        return "Restarting the system"
    else:
        return get_openrouter_response(command)

# 🚀 Main logic
if __name__ == "__main__":
    speak("Hello Mahesh Sir, I am your Jarvis. Which language should I speak?", 'en')
    lang = listen_command().lower()

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
        command = listen_command()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!", lang_code)
                break
            result = execute_command(command)
            print("🤖 Jarvis:", result)
            speak(result, lang_code)
