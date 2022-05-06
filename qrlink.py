import qrcode
from PIL import Image

qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )

qr.clear()
qr.add_data('TEXT')

qr.make(fit=True)

img = qr.make_image(fill_color="#000000", back_color="#FFFFFF")
img.save('PATH')
