import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text to convert to audio
text_to_speak = " This is a small demonstration .pdf file  "

# Convert text to audio and play it
engine.say(text_to_speak)
engine.runAndWait()
