# Printed_Character_Recognition

Project: Printed Document OCR Extractor

This project is a **Python-based OCR (Optical Character Recognition) tool** that extracts text from printed documents in multiple formats such as **PDF, DOCX, JPG, and PNG**. It leverages **Tesseract OCR** along with image preprocessing techniques to improve text recognition accuracy.

 🔑 Features:

* 🖼️ **Image Processing** – Converts images to grayscale, enhances contrast, resizes, and applies thresholding for better OCR accuracy.
* 📷 **Image to Text** – Extracts text from scanned images (JPG, PNG).
* 📑 **PDF to Text** – Converts each page of a PDF into images and applies OCR.
* 📝 **DOCX to Text** – Reads Word documents and extracts text directly.
* 💾 **Save Results** – Option to save extracted text into a `.txt` file.
* ✅ **Cross-format Support** – Works seamlessly across PDF, DOCX, and image formats.

 🛠️ Technologies Used:

* Python
* pytesseract (Tesseract OCR)
* Pillow (PIL)
* pdf2image
* python-docx

 🚀 How It Works:

1. User provides the file path (PDF, DOCX, or Image).
2. Script preprocesses and extracts text using OCR.
3. Extracted text is displayed on the console.
4. User can choose to save the text into a file.



