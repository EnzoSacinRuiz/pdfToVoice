import pyttsx3
from gtts import gTTS

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Read the extracted text from the text file
with open('extracted_text.txt', 'r', encoding='utf-8') as text_file:
    text_to_speak = text_file.read()

# Convert text to audio using gTTS
tts = gTTS(text_to_speak)

# Save the audio as an MP3 file
tts.save('output.mp3')

# Play the audio (optional)
# You can use other libraries like pygame to play the MP3 file if needed.

print("Text converted to audio and saved as 'output.mp3'")
