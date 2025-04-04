import os
import subprocess

folder_path = '/'

for file_name in os.listdir(folder_path):
    if file_name.endswith('.png'):
        file_path = os.path.join(folder_path, file_name)
        print(f'Оптимизация файла: {file_path}')

        subprocess.run(['optipng', '-o2', file_path])

print('Оптимизация завершена!')
