import os
import PyPDF2

# Get the current directory path
current_dir = os.getcwd()  # Using a more descriptive variable name
print(f"Current directory: {current_dir}")  # Print the current directory for reference

# Get the filenames in the directory
filenames = os.listdir(current_dir)  # Store filenames in a clear variable

def combine_pdfs(pdf_list):
    """
    This function combines PDF files from a specified directory.
    Args:
        pdf_list (list): A list of filenames containing PDFs.
    Returns:
        None (creates a new PDF file named 'super.pdf' in the current directory).
    """

    merger = PyPDF2.PdfMerger()
    for filename in pdf_list:
        # Check if file extension is '.pdf' (case-insensitive)
        if filename.lower().endswith('.pdf'):
            merger.append(filename)

    # Write the merged PDF to a file named 'super.pdf'
    merger.write('super.pdf')
    print(f"Merged PDF created: super.pdf")  # Informative message


# Call the combine_pdfs function with the list of filenames
combine_pdfs(filenames)

