import os
from PyPDF2 import PdfReader,PdfWriter
reader = PdfReader("D:/Python-lang/76-Day-76-Exercise-8/sample/sample1.pdf")
page = reader.pages[0]
page = reader.pages[1]
print(page.extract_text())


pdf_folder = "D:/Python-lang/76-Day-76-Exercise-8/sample"
pdf_files = [os.path.join(pdf_folder,file) for file in os.listdir(pdf_folder) if file.endswith(".pdf")]
print(pdf_folder)
print(pdf_files)

merger = PdfWriter()
for pdf in pdf_files:
    merger.append(pdf)

merger.write("D:/Python-lang/76-Day-76-Exercise-8/sample/Merged.pdf")
merger.close()

# from pathlib import Path
# files = Path("D:/Python-lang/76-Day-76-Exercise-8")

