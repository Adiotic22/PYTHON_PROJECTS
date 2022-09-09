import qrcode
qr=qrcode.QRCode(version=15,box_size=10,border=5)
qr.add_data("https://www.google.com/")
qr.make(fit=True)
generate_image=qr.make_image(fill_color="black",back_color="white")
generate_image.save("image1.png")

