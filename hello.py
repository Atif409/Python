import fitz  # PyMuPDF
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def pdf_to_word(pdf_path, docx_path):
    # Load the PDF using PyMuPDF
    pdf_document = fitz.open(pdf_path)
    
    # Create a Word document using python-docx
    doc = Document()
    
    for page in pdf_document:
        text = page.get_text("text")
        
        # Create a new paragraph in the Word document
        paragraph = doc.add_paragraph(text)
        
        # Apply styling
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # Adjust alignment
        
        # You can add more styling options as needed
        
        # Add a page break after each page
        doc.add_page_break()
    
    # Save the Word document
    doc.save(docx_path)

# Convert the PDF to Word with styling
pdf_to_word("sample.pdf", "output.docx")
