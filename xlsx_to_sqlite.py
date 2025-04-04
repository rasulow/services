from datetime import datetime
import pandas as pd
import sqlite3


file_path = 'jemi.xlsx'
db_path = 'db.sqlite3'

# df = pd.read_excel(file_path, skiprows=22)

# tuple_rows = list(df.itertuples(index=False, name=None))
# data_list = []
# table_name = 'local_book'

# for row in tuple_rows:
#     name = row[3]
#     income = row[1]
#     published_year = row[5]
#     pages = row[6]
#     if isinstance(income, datetime):
#         income = income.strftime("%d.%m.%Y")
#     else:
#         income = income.split(' ')[0].replace(',', '.').replace('..', '.')
        
#     data_list.append((name, income, published_year, pages, True, datetime.now(), datetime.now()))
        
# insert_query = f"INSERT INTO {table_name} (name, income, published_year, pages, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)"
    
conn = sqlite3.connect(db_path)

cur = conn.cursor()


cur.execute("SELECT * FROM local_book")
rows = cur.fetchall()
for row in rows:
    print(row)