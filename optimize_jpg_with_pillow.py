import os
from PIL import Image

folder_path = '/'

for file_name in os.listdir(folder_path):
    if file_name.lower().endswith(('.jpg', '.jpeg')):
        file_path = os.path.join(folder_path, file_name)
        print(f'Оптимизация файла: {file_path}')

        with Image.open(file_path) as img:
            img.save(file_path, 'JPEG', optimize=True, quality=85)

print('Оптимизация завершена!')
