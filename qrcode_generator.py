import qrcode

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=1)

qr.add_data("https://www.google.com/") # insert any link link here and run the program
qr.make(fit=True)

img = qr.make_image()
img.save("something.png") # you can rename the QR code however you want
