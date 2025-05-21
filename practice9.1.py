from PIL import Image

image_path = "fonstola.ru_331881.jpg"

try:

    with Image.open(image_path) as img:
        img.show()

        width, height = img.size

        print(f"1. Размер: {width}x{height} пикселей")
        print(f"2. Формат: {img.format}")
        print(f"3. Цветовая модель: {img.mode}")

except FileNotFoundError:
    print(f"Ошибка: файл '{image_path}' не найден!")
