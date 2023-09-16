import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Read the extracted text from the text file
with open('extracted_text.txt', 'r', encoding='utf-8') as text_file:
    text_to_speak = text_file.read()

# Convert text to audio and play it
engine.say(text_to_speak)
engine.runAndWait()
