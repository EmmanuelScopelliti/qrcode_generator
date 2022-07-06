
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

number = '123456789012'
code = EAN13(number, writer=ImageWriter())
code.save("barcodeArt1")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data('SW10001')
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
).convert('RGB')

img.save("art1.png")