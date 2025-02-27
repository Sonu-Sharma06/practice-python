
import qrcode as qr
from PIL import Image 

qr_img=qr.QRCode(version=1,
                 error_correction=qr.constants.ERROR_CORRECT_H,
                 box_size=6,border=4,)
qr_img.add_data("https://youtu.be/i9SBfFt8soY?si=m26bGAP2gbeGwywR")
qr_img.make(fit=True)

new_img=qr_img.make_image(fill_color="red",back_color="white")

new_img.save("edited.png")