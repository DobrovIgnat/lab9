from PIL import Image

def process_image(original_path):
    try:

        with Image.open(original_path) as img:

            small_size = (img.width // 3, img.height // 3)
            small_img = img.resize(small_size)
            small_img.save('small_' + original_path)
            print(f"Уменьшенная копия'small_{original_path}'")

            horizontal_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
            horizontal_mirror.save('horizontal_' + original_path)
            print(f"Горизонтально'horizontal_{original_path}'")

            vertical_mirror = img.transpose(Image.FLIP_TOP_BOTTOM)
            vertical_mirror.save('vertical_' + original_path)
            print(f"Вертикально как 'vertical_{original_path}'")

    except FileNotFoundError:
        print(f"Ошибка: файл '{original_path}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

image_name = "fonstola.ru_331881.jpg"
process_image(image_name)