import cv2
import pytesseract
from PIL import Image, ImageDraw, ImageFont

#pytesseract executable is required here..
pytesseract.pytesseract.tesseract_cmd= "C:\\Users\\stefan\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Load the image and apply OCR to the image
image = Image.open(r'C:\Users\stefan\Desktop\lorem_ipsum.png')
text = pytesseract.image_to_string(image)

# Create a drawing object and set the font
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 20)

# Get the bounding boxes of the detected text
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

# Draw a box around each word
for i in range(len(data['text'])):
    if int(data['conf'][i]) > 60:  # Only draw boxes around words with high confidence
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        draw.rectangle((x, y, x + w, y + h), outline='red', width=2)
        draw.text((x, y - 20), data['text'][i], font=font, fill='orange')

image.show()
