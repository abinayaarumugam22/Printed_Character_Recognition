import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
from pdf2image import convert_from_path
from docx import Document

# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # update if needed

def preprocess_image(image_path):
    """Preprocess image to improve OCR accuracy."""
    image = Image.open(image_path)
    # Convert to grayscale
    image = image.convert('L')
    # Increase contrast
    image = ImageOps.autocontrast(image)
    # Resize to enhance small text
    image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)
    # Apply thresholding
    image = image.point(lambda x: 0 if x < 150 else 255, '1')
    return image

def extract_text_from_image(image_path):
    """Extract text from an image using OCR with preprocessing."""
    try:
        preprocessed_image = preprocess_image(image_path)
        text = pytesseract.image_to_string(preprocessed_image)
        return text
    except Exception as e:
        return f"Error processing image: {e}"

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF using OCR."""
    try:
        pages = convert_from_path(pdf_path)
        text = ''
        for i, page in enumerate(pages):
            temp_filename = f"page_{i}.png"
            page.save(temp_filename, 'PNG')
            text += extract_text_from_image(temp_filename) + '\n'
            os.remove(temp_filename)
        return text
    except Exception as e:
        return f"Error processing PDF: {e}"

def extract_text_from_docx(docx_path):
    """Extract text from a Word document."""
    try:
        doc = Document(docx_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error processing DOCX: {e}"

def main():
    """Main function to execute the OCR text extraction."""
    print("📄 Printed Document OCR Extractor")
    file_path = input("Enter the full path of the file (PDF, DOCX, JPG, PNG): ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    # Process the file based on its extension
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        result = extract_text_from_image(file_path)
    elif file_path.lower().endswith('.pdf'):
        result = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        result = extract_text_from_docx(file_path)
    else:
        print("❌ Unsupported file format. Please use PDF, DOCX, PNG, or JPG.")
        return

    # Display the extracted text
    print("\n📝 Extracted Text:\n")
    print(result)

    # Ask to save the result
    save = input("\nDo you want to save the extracted text to a file? (y/n): ").lower()
    if save == 'y':
        output_file = "extracted_text.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✅ Text saved to {output_file}")
        print("📂 Full path:", os.path.abspath(output_file))
    else:
        print("❌ Text not saved.")

    print("✅ completed.......!")

if __name__ == "__main__":
    main()
