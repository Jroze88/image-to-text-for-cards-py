try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_top(filename):



    im = Image.open(filename)

    width, height = im.size

    left = 0
    top = 0
    right = 0
    bottom = 300

    imSize = im.crop((left, top, right, bottom))

    text = pytesseract.image_to_string(Image.open(imSize))  
    return text  
