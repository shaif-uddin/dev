import os
import PyPDF2

filenames = os.listdir(os.getcwd())
print(filenames)


def merger(plist):
    merge_file = PyPDF2.PdfMerger()
    for file in plist:
        if file.lower().endswith('.pdf'):
            merge_file.append(file)
    merge_file.write('super.pdf')


merger(filenames)
