#Crea_Logo_Circular1.py

from PIL import Image, ImageDraw

# Cargar y redimensionar el logo
logo_path = "logo.png"  # Ruta de la imagen original del logo
logo_size = 80  # Tamaño deseado para el logo
logo = Image.open(logo_path).resize((logo_size, logo_size)).convert("RGBA")

# Crear una máscara circular para el logo
mask = Image.new("L", (logo_size, logo_size), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.ellipse((0, 0, logo_size, logo_size), fill=255)

# Crear una imagen circular con fondo transparente
circular_logo = Image.new("RGBA", (logo_size, logo_size))
circular_logo.paste(logo, (0, 0), mask=mask)

# Guardar el logo circular en un archivo (opcional)
circular_logo.save("logo_circular.png")  # Guarda el logo con transparencia circular
