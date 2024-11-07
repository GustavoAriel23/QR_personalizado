import qrcode
from PIL import Image
import pandas as pd

# Cargar el logo
logo_path = "logo.png"  # Asegúrate de tener un logo cuadrado y en formato PNG
logo = Image.open(logo_path)

# Redimensionar el logo
logo_size = 80  # Tamaño del logo
logo = logo.resize((logo_size, logo_size))

# Leer base de datos
df = pd.read_csv("data.csv")  # Asegúrate de tener una columna "code" en el archivo CSV

for index, row in df.iterrows():
    code = row["code"]
    url = f"https://kibbo.io/?c={code}"
    
    # Generar el QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=15,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen QR y agregar logo
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")
    qr_width, qr_height = qr_img.size
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, pos)

    # Guardar la imagen QR
    qr_img.save(f"QRS_PNG/QR_{code}.png")
