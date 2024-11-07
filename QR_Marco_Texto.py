#QR_Marco_Texto.py
import qrcode
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Cargar el logo redondo previamente creado
logo_path = "logo_circular.png"
logo = Image.open(logo_path)

# Redimensionar el logo si es necesario
logo_size = 80
logo = logo.resize((logo_size, logo_size))

# Leer la base de datos
df = pd.read_csv("data.csv")

# Configuración de fuente para el texto
try:
    font = ImageFont.truetype("arial.ttf", 14)
except IOError:
    font = ImageFont.load_default()

# Definir el grosor y color del marco
frame_thickness = 10  # Grosor del marco
frame_color = "black"  # Color del marco

for index, row in df.iterrows():
    code = row["code"]
    url = f"https://xxxx.io/?c={code}"

    # Generar el QR con personalizaciones
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=12,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen QR con color personalizado
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGBA")

    # Calcular posición y añadir logo redondo al QR
    qr_width, qr_height = qr_img.size
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, pos, mask=logo)

    # Crear espacio extra para el texto debajo del QR
    text_space = 30
    new_height = qr_height + text_space
    qr_with_text = Image.new("RGB", (qr_width, new_height), "white")
    qr_with_text.paste(qr_img, (0, 0))

    # Añadir el texto debajo del QR
    draw = ImageDraw.Draw(qr_with_text)
    text_bbox = draw.textbbox((0, 0), code, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (qr_width - text_width) // 2
    text_y = qr_height + 2
    draw.text((text_x, text_y), code, font=font, fill="black")

    # Añadir un marco alrededor de la imagen QR con el texto
    framed_width = qr_width + 2 * frame_thickness
    framed_height = new_height + 2 * frame_thickness
    framed_image = Image.new("RGB", (framed_width, framed_height), frame_color)

    # Pegar el QR con el texto dentro del marco
    framed_image.paste(qr_with_text, (frame_thickness, frame_thickness))

    # Guardar la imagen final con marco en la carpeta especificada
    framed_image.save(f"cuerres/QR_{code}_framed.png")
