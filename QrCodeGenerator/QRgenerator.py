import qrcode
import qrcode.constants

qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 4)
URL = input("Enter the URL to generate the QRcode: ")
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color = (0,0,0), back_color = (255,255,255))

# The QRcode will be automatically saved in your File path.