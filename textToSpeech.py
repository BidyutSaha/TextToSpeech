import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(
    "Please subscribe the channel and press the bell button to get updated. Thank you ")
engine.runAndWait()
