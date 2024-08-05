from PIL import Image
import os

def dividir_guardar_imagen(ruta_imagen, carpeta_destino, divisiones_por_columnas):
    # Cargar la imagen
    try:
        img = Image.open(ruta_imagen)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar la imagen en {ruta_imagen}")
        return

    ancho, alto = img.size

    # Calcular el número de divisiones
    tamano_cuadrado = ancho // divisiones_por_columnas
    divisiones_por_fila = alto // tamano_cuadrado

    # Crear carpeta de destino
    os.makedirs(carpeta_destino, exist_ok=True)

    contador = 0
    for i in range(divisiones_por_fila):
        for j in range(divisiones_por_columnas):
            # Coordenadas del cuadrado
            izquierda = j * tamano_cuadrado
            superior = i * tamano_cuadrado
            derecha = izquierda + tamano_cuadrado
            inferior = superior + tamano_cuadrado

            # Cortar y guardar el cuadrante
            cuadrado = img.crop((izquierda, superior, derecha, inferior))
            nombre_archivo = f"tile ({contador + 1}).png"
            cuadrado.save(os.path.join(carpeta_destino, nombre_archivo))
            contador += 1

# Llamada a la función con los valores adecuados
dividir_guardar_imagen("assets/images/tiles/Dungeon_Tileset.png", "assets/images/tiles/", 10)