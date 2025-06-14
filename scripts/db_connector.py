import mysql.connector
from mysql.connector import Error

def create_connection():
    """Создаёт и возвращает подключение к базе данных MySQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Или можно использовать "127.0.0.1"
            port=3306,  # Порт по умолчанию для MySQL
            database="projectsви",  # Имя базы данных
            user="root",  # Имя пользователя для подключения
            password="NewStrongPassword"
        )
        
        if connection.is_connected():
            print("Успешное подключение к базе данных")
            return connection
    
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None

def close_connection(connection):
    """Закрывает соединение с базой данных."""
    if connection and connection.is_connected():
        connection.close()
        print("Соединение с базой данных закрыто")
