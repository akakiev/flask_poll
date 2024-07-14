# Опис: Описує моделі даних, які використовуються в додатку
#     для зберігання опитувань та варіантів відповідей
from app import db

# Клас Survey описує модель опитування
# Клас містить поля id, question та options
# Поле id є унікальним ідентифікатором опитування
# Поле question містить питання опитування
# Поле options містить варіанти відповідей на питання
class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.relationship('Option', backref='survey', lazy=True)

# Клас Option описує модель варіанту відповіді
# Клас містить поля id, option_text, votes та survey_id
# Поле id є унікальним ідентифікатором варіанту відповіді
# Поле option_text містить текст варіанту відповіді
# Поле votes містить кількість голосів за варіант відповіді
# Поле survey_id є зовнішнім ключем, який посилається на id опитування
#     до якого відноситься варіант відповіді
class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_text = db.Column(db.String(100), nullable=False)
    votes = db.Column(db.Integer, default=0)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
