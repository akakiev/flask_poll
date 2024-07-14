# Опис: Конфігураційний файл додатку
# Цей файл містить клас Config, який містить налаштування додатку
# Цей клас містить налаштування для бази даних та секретного ключа
# Для роботи додатку використовується база даних SQLite
# Секретний ключ використовується для шифрування сесій користувачів
import os

# Отримання шляху до поточної директорії
basedir = os.path.abspath(os.path.dirname(__file__))

# Клас Config містить налаштування додатку
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
