import io
from PyPDF2 import PdfReader, PdfWriter


def merge_pdf_with_page(pdf_file, page_file, position):
    input_pdf = PdfReader(pdf_file)
    input_page = PdfReader(page_file).pages[0]  # Get the first page from the page file

    output_pdf = PdfWriter()
    page_count = len(input_pdf.pages)

    # Add the pages from the original PDF up to the specified position
    for i in range(position):
        if i < page_count:
            output_pdf.add_page(input_pdf.pages[i])

    # Insert the page from the page file at the specified position
    output_pdf.add_page(input_page)

    # Add the remaining pages from the original PDF
    for i in range(position, page_count):
        output_pdf.add_page(input_pdf.pages[i])

    # Create a new PDF file in memory
    output_buffer = io.BytesIO()
    output_pdf.write(output_buffer)
    output_buffer.seek(0)

    return output_buffer
