from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Import routes
from routes import student_routes, teacher_routes

app.register_blueprint(student_routes)
app.register_blueprint(teacher_routes)

if __name__ == '__main__':
    app.run(debug=True)
