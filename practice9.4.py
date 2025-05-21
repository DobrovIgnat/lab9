from PIL import Image, ImageDraw, ImageFont
import os

if not os.path.exists('watermarked'):
    os.mkdir('watermarked')

watermark_text = "its my"

for i in range(1, 6):
    try:
        img = Image.open(f'{i}.jpg')

        draw = ImageDraw.Draw(img)

        font = ImageFont.load_default().font_variant(size=40)

        draw.text((50, 50), watermark_text, fill='white', font=font)

        img.save(f'watermarked/{i}_with_watermark.jpg')
        print(f'Обработано: {i}.jpg')

    except:
        print(f'Ошибка с файлом {i}.jpg')
