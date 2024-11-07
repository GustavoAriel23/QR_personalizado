#Crea_Logo_Circular.py

from PIL import Image, ImageDraw

# Cargar el logo y redimensionarlo
logo_path = "logo_cuad.png"  # Ruta de la imagen original del logo
logo_size = 80  # Tamaño deseado para el logo
logo = Image.open(logo_path).resize((logo_size, logo_size))

# Crear una máscara circular para el logo
mask = Image.new("L", (logo_size, logo_size), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.ellipse((0, 0, logo_size, logo_size), fill=255)

# Aplicar la máscara circular al logo
logo.putalpha(mask)

# Guardar el logo circular en un archivo (opcional)
logo.save("logo_circular.png")  # Guarda el logo con transparencia circular