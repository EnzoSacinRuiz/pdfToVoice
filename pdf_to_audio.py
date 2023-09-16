import PyPDF2
import pyttsx3
from gtts import gTTS
from pydub import AudioSegment

# Extract text from the PDF file
pdf_file_path = 'sample.pdf'

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    extracted_text = ''

    for page in pdf_reader.pages:
        extracted_text += page.extract_text()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Convert text to audio
engine.save_to_file(extracted_text, 'temp.mp3')
engine.runAndWait()

# Load the temporary audio file
audio = AudioSegment.from_mp3('temp.mp3')

# Export the audio as an MP3 file
audio.export('output.mp3', format='mp3')

# Remove the temporary audio file
import os
os.remove('temp.mp3')

print("Text converted to audio and saved as 'output.mp3'")
