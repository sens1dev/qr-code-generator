import qrcode

data = input('Enter the text or URL: ').strip()
filename = f"{input('Enter the filename: ').strip()}.png"
qr = qrcode.QRCode(box_size=10, border=1)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')