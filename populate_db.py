from app import app, db
from app.models import Survey, Option

def populate_db():
    with app.app_context():
        # Create some sample surveys
        survey1 = Survey(question="What's your favorite programming language?")
        survey2 = Survey(question="What's your favorite web framework?")

        # Add options to the first survey
        survey1.options.append(Option(option_text="Python"))
        survey1.options.append(Option(option_text="JavaScript"))
        survey1.options.append(Option(option_text="Java"))
        survey1.options.append(Option(option_text="C++"))

        # Add options to the second survey
        survey2.options.append(Option(option_text="Flask"))
        survey2.options.append(Option(option_text="Django"))
        survey2.options.append(Option(option_text="Express"))
        survey2.options.append(Option(option_text="Spring"))

        # Add the surveys to the session
        db.session.add(survey1)
        db.session.add(survey2)

        # Commit the session
        db.session.commit()

if __name__ == '__main__':
    populate_db()
