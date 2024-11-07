#python generador_qr.py

import qrcode
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Cargar el logo
logo_path = "logo.png"
logo = Image.open(logo_path)

# Redimensionar el logo
logo_size = 75
logo = logo.resize((logo_size, logo_size))

# Leer base de datos
df = pd.read_csv("data.csv")

# Configuración de fuente para el texto (ajusta el tamaño de fuente según sea necesario)
try:
    font = ImageFont.truetype("arial.ttf", 24)  # Usar Arial (asegúrate de tener Arial o cambia a otra fuente disponible)
except IOError:
    font = ImageFont.load_default()  # Cargar fuente predeterminada si Arial no está disponible

for index, row in df.iterrows():
    code = row["code"]
    url = f"https://kibbo.io/?c={code}"

    # Generar el QR con personalizaciones
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=12,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen QR con color personalizado
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

    # Calcular posición y añadir logo al QR
    qr_width, qr_height = qr_img.size
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, pos)

    # Ampliar la imagen para dejar espacio para el texto debajo del QR
    new_height = qr_height + 30  # Aumenta 30 píxeles para el texto
    qr_with_text = Image.new("RGB", (qr_width, new_height), "white")
    qr_with_text.paste(qr_img, (0, 0))

    # Escribir el código debajo del QR
    draw = ImageDraw.Draw(qr_with_text)
    text_bbox = draw.textbbox((0, 0), code, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (qr_width - text_width) // 2
    text_y = qr_height + 0  # Coloca el texto un poco debajo del QR
    draw.text((text_x, text_y), code, font=font, fill="black")

    # Guardar la imagen QR con el texto en la carpeta especificada
    qr_with_text.save(f"QRS_PNG/QR_{code}.png")
