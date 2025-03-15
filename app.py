import pytesseract
from PIL import Image
from flask import Flask, request, jsonify

def extract_text(image_path):
    # Open the image using PIL
    pil_image = Image.open(image_path)

    # Perform OCR using Tesseract’s built-in image processing
    extracted_text = pytesseract.image_to_string(
        pil_image, config="--psm 4 --oem 3"
    )

    return extracted_text.strip()



app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image_file = request.files['image']
    image_path = "temp_image.png"
    image_file.save(image_path)

    # Extract text using Tesseract’s native processing
    text = extract_text(image_path)
    
    return jsonify({'extracted_text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
