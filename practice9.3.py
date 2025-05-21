from PIL import Image, ImageFilter
import os


def apply_filter_to_images():
    output_dir = "измененные картинки"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, 6): #номера картинок 1-5
        input_path = f"{i}.jpg"
        output_path = f"{output_dir}/izmeneno_{i}.jpg"

        try:
            with Image.open(input_path) as img:

                filtered_img = img.filter(ImageFilter.FIND_EDGES)

                filtered_img.save(output_path)
                print(f"Обработано: {input_path} -> {output_path}")

        except FileNotFoundError:
            print(f"Файл {input_path} не найден!")
        except Exception as e:
            print(f"Ошибка при обработке {input_path}: {e}")


apply_filter_to_images()