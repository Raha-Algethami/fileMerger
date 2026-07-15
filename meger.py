from pypdf import PdfWriter
import os

merger = PdfWriter()

# 2/ Look at every file in the current folder (represented by '.')
for file in os.listdir('.'):

    # 3/ Only grab the files that end with .pdf
    if file.endswith(".pdf"):
        print(f"Grabbing {file}...")
        merger.append(file)

# 4/  Write all the grabbed pages into one final document
merger.write("Combined_Document.pdf")
merger.close()

print("Done! Your merged file is ready")
