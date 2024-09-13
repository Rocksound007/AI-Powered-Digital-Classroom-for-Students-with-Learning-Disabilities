from flask import Blueprint, jsonify, request
from models import db, User, Lesson

student_routes = Blueprint('students', __name__)
teacher_routes = Blueprint('teachers', __name__)

@student_routes.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = User(name=data['name'], role='student', email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully!"})

@teacher_routes.route('/lessons', methods=['POST'])
def add_lesson():
    data = request.get_json()
    new_lesson = Lesson(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(new_lesson)
    db.session.commit()
    return jsonify({"message": "Lesson added successfully!"})
