import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

data_to_encode = input("Enter data to encode in QR code: ")
file_name = input("Enter the file name to save the QR code (with extension, e.g., image.png): ")

generate_qr_code(data_to_encode, file_name)
print(f"QR code saved as {file_name}")
