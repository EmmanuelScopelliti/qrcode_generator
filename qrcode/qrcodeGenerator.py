
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

# Barcode Generator
number = 'your EAN here'
code = EAN13(number, writer=ImageWriter())
code.save("barcodeArt1")

# qrcode generator
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data('Your Text/url here')
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
).convert('RGB')

img.save("art1.png")
