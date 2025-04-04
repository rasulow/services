import os
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

folder_path = 'media/lessons/'

folder_files = os.listdir(folder_path)

for file in folder_files:
    if file in ('.idea', 'main.py', 'db.sqlite3'):
        continue

    file_path = os.path.join(folder_path, file)

    cursor.execute('SELECT * FROM lesson WHERE material LIKE ?', ('%' + file + '%',))
    results = cursor.fetchall()

    if not results:
        if os.path.isfile(file_path):
            os.remove(file_path)

conn.close()

