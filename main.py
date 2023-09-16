import PyPDF2

pdf_file_path = 'sample.pdf'

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    extracted_text = ''

    for page in pdf_reader.pages:
        extracted_text += page.extract_text()

# Print or use extracted_text as needed
print(extracted_text)




