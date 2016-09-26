from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os
import argparse

def parser_func():
  parser = argparse.ArgumentParser(description='PDF reconstructor')
  parser.add_argument('--outname', '-o', default='out.pdf', help='Output file name')
  parser.add_argument('--dir', default='', help='Directory with pdfs')
  return parser

def pdf_processor(filename, pdfs, path=""):
  if path == "":
    script_dir = os.path.dirname(__file__)
  else:
    script_dir = path
  output = PdfFileWriter()
  for pdf in pdfs:
    abs_file_path = os.path.join(script_dir, pdf)
    infile = PdfFileReader(abs_file_path, 'rb')
    p = infile.getPage(0)
    if p.getContents(): # getContents is None if  page is blank
      output.addPage(p)
  outfullpath = os.path.join(script_dir, filename)
  with open(outfullpath, 'wb') as f:
   output.write(f)

def main():
  parser = parser_func()
  args = parser.parse_args()
  if os.path.isdir(args.dir)== False:
    os.mkdir(args.dir)
	
  output_file = args.outname
  pdfs = []
  for file in os.listdir(args.dir):
    if file.endswith(".pdf"):
	  pdfs.append(file)
  pdf_processor(output_file, pdfs, args.dir)  
  
if __name__ == '__main__':
  main()
