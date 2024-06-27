import os

import PyPDF2

# Get the current directory path
getdir = os.getcwd();
# Get the file name in the directory
getfilename = os.listdir(getdir)


def combiner(plist):
    merger=PyPDF2.PdfMerger()
    for filename in plist:
        # Get a list of files with the .pdf extension
        if filename.endswith('.pdf'):
            merger.append(filename)
    merger.write('super.pdf')


combiner(getfilename)
