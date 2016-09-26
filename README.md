# pdf_processor
Sometimes we just want to read the abstract of a bunch of papers. This program helps extract the first pages of all pdfs in the current directory and merge them into a big pdf file. (Thus, we can save time clicking/opening each file at a time.)

**Notice:** This program only gets pdf files under current directory. It will not dig into sub-directory to find pdf files.

# Dependency
PyPDF2: https://github.com/mstamy2/PyPDF2

# How to use
Linux: `python pdf.py --outname [output file name] --dir [input file directory]`

Windows: `C:\python27\python.exe [path to pdf.py] --outname [output file name] --dir [input file directory full path]`


