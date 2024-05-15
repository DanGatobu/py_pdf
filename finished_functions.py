from pypdf import PdfReader
from pypdf import PdfWriter


def merge(links,output_name):
    merger = PdfWriter()
    for i in links:
        
        merger.append(fileobj=i[0])
        
    merger.write(f'{output_name}.pdf')
    

def encrypt_pdf(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    writer = PdfWriter(clone_from=reader)
    writer.encrypt(password, algorithm="AES-256")
    with open(output_pdf, "wb") as f:
        writer.write(f)
        
def decrypt_pdf(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    if reader.is_encrypted:
        reader.decrypt(password)
    writer = PdfWriter(clone_from=reader)
    with open(output_pdf, "wb") as f:
        writer.write(f)



def compress_remove_duplicates(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter(clone_from=reader)
    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(reader.metadata)

    with open(f"{output_pdf}.pdf", "wb") as fp:
        writer.write(fp)


def compress_remove_images(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter(clone_from=reader)
    for page in reader.pages:
        writer.add_page(page)

    writer.remove_images()

    with open(f"{output_pdf}.pdf", "wb") as fp:
        writer.write(fp)
        
        
def compress_reduceimage_quality(input_pdf, output_pdf, quality):
    reader = PdfReader(input_pdf)
    writer = PdfWriter(clone_from=reader)
    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=quality)

    with open(f"{output_pdf}.pdf", "wb") as f:
        writer.write(f)
        
def lossless_compression(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter(clone_from=reader)
    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        page.compress_content_streams()

    with open(f"{output_pdf}.pdf", "wb") as f:
        writer.write(f)
        
    
def extract_text(pdf,pdf_name):
    reader = PdfReader(pdf)
    
    l=''
    for page in reader.pages:
        
        l+=page.extract_text()
    l=l.encode('utf-8')
    with open(f"{pdf_name}.txt", "wb") as f:
        f.write(l)
        
    
    return l
        