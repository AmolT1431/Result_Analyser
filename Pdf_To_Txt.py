import PyPDF2
import os


def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

directory_path = r"F:\C & C++\Python\pdf"

files = os.listdir(directory_path)
file_paths = [os.path.join(directory_path, file) for file in files]
for file_path in file_paths:
    out=file_path.replace("pdf","Txt")
    extract_text_from_pdf(file_path, out)
