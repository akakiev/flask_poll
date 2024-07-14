# В цьому файлі ми ініціалізуємо нашу програму та базу даних
# Імпортуємо клас Flask з модуля flask
# Імпортуємо клас SQLAlchemy з модуля flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Створюємо екземпляр класу Flask
app = Flask(__name__)

# Імпортуємо конфігурацію з файлу config.py
app.config.from_object('config.Config')

# Створюємо екземпляр класу SQLAlchemy
db = SQLAlchemy(app)

with app.app_context():
    from app import routes, models
    db.create_all()

# Імпортуємо модулі з пакету app
#from app import routes, models

# Створюємо таблиці в базі даних
#db.create_all()
