import qrcode  
from PIL import Image 

qr = qrcode.QRCode(version= 1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size= 12, border = 4)


qr.add_data("https://github.com/PareshZodape")
qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save("QR code.png")
