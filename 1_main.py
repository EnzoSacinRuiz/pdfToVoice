import PyPDF2

pdf_file_path = 'this.pdf'

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    extracted_text = ''

    for page in pdf_reader.pages:
        extracted_text += page.extract_text()

# Print or use extracted_text as needed
print(extracted_text)

# Save the extracted text to a text file
with open('extracted_text.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(extracted_text)





