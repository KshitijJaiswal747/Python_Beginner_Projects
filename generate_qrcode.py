import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter filename (e.g., qr.png): ").strip()

fill = input("Enter QR color (black, Blue, Red, Green, etc.): ").strip()
background = input("Enter background color (White, Yellow, etc.): ").strip()

qr = qrcode.QRCode(
    
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_color=fill,
    back_color=background
)

img.save(filename)

print("QR Code Generated Successfully!")
print(f"Saved as {filename}")