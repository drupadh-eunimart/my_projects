from flask import jsonify, request
from flaskApp import db, schema
from flaskApp.models.student import Student
from flaskApp.utils.errorHandler import handle_error
from flaskApp.utils.schema import studentSchema


class StudentServices:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StudentServices, cls).__new__(cls)
        return cls._instance

    @handle_error
    def getStudent(self):
        rNo = request.args.get('rNo')
        if rNo:
            student = Student.query.filter_by(rNo=rNo).first()
            return jsonify(success=True, student=student.as_dict())
        else:
            students = Student.query.all()
            students = list(map(Student.as_dict, students))
            return jsonify(success=True, students=students)

    @handle_error
    @schema.validate(studentSchema)
    def addStudent(self):
        rNo, firstName, lastName, dept = request.json.get('rNo'), request.json.get('firstName'), request.json.get('lastName'), request.json.get('dept')
        student = Student(rNo=rNo, firstName=firstName, lastName=lastName, dept=dept)
        db.session.add(student)
        db.session.commit()
        return jsonify(success=True, student=student.as_dict())

    @handle_error
    def updateStudent(self):
        rNo = request.args.get('rNo')
        firstName, lastName, dept = request.json.get('firstName'), request.json.get('lastName'), request.json.get('dept')
        student = Student.query.filter_by(rNo=rNo).first()
        if firstName: student.firstName = firstName
        if lastName: student.lastName = lastName
        if dept: student.dept = dept
        db.session.commit()
        return jsonify(success=True, student=student.as_dict())

    @handle_error
    def deleteStudent(self):
        rNo = request.args.get('rNo')
        student = Student.query.filter_by(rNo=rNo).first()
        db.session.delete(student)
        db.session.commit()
        return jsonify(success=True)

