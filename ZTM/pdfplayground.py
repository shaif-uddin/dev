import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Create a new PdfWriter object
    writer = PyPDF2.PdfWriter()

    # Get the first page from the reader
    page = reader.pages[0]

    # Rotate the page by 180 degrees
    page.rotate(180)

    # Add the rotated page to the writer
    writer.add_page(page)

    # Write the modified content to a new PDF file
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

print(f"Successfully created 'tilt.pdf' with the first page rotated.")

