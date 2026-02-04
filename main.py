from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs = []

n = int(input("How many PDFs do you want to merge: "))

for i in range(n):
    name = input(f"Enter the name of PDF {i+1} (with .pdf extension): ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged_pdf.pdf")
merger.close()

print("✅ PDFs merged successfully into Merged_pdf.pdf")
