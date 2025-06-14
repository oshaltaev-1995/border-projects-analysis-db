import pandas as pd
import mysql.connector
from openpyxl import Workbook
from pandas import ExcelWriter

# Подключение к базе данных через mysql.connector
db_config = {
    'host': 'localhost',
    'database': 'projectsdb',
    'user': 'root',
    'password': 'NewStrongPassword'
}

# Устанавливаем соединение
conn = mysql.connector.connect(**db_config)

# Получаем список всех таблиц из базы
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]

# Создаём Excel-файл
with ExcelWriter("all_tables.xlsx", engine="openpyxl") as writer:
    for table in tables:
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        df.to_excel(writer, sheet_name=table, index=False)

print("✅ Все таблицы успешно экспортированы в all_tables.xlsx")

# Закрываем соединения
cursor.close()
conn.close()
