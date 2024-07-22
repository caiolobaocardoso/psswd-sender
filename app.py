import pyautogui
from pdf2image import convert_from_path
import keras_ocr

#pdf to image
pdf_path = 'C:/Users/042000026/Documents/workspace/psswd-sender/pdf-exemplo.pdf'
pages = convert_from_path(pdf_path)


#ocr
pipeline = keras_ocr.pipeline.Pipeline()
images = pages
predictions = pipeline.recognize(images) 

#display 

for image, predictions in zip(images, predictions):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions)