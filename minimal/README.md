# Minimal examples of embedding files in PDF/A

This folder contains two examples of embedding files in a PDF/A document: `ex.tex` embeds the text file `attachme.txt`; `ex_xlsx.tex` embeds the XLSX file `xl.xlsx`.
The PDF files produced are `ex.pdf` and `ex_xlsx.pdf` respectively.

A pair of Python scripts show how the embedded files may be extracted.
`read_attachment.py` extracts the text file, and `read_xlsx.py` extracts the spreadsheet.