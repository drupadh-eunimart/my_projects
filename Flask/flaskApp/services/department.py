from flask import jsonify, request
from flaskApp import db, schema
from flaskApp.models.department import Department
from flaskApp.models.student import Student
from flaskApp.utils.errorHandler import handle_error
from flaskApp.utils.schema import departmentSchema


class DepartmentServices:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DepartmentServices, cls).__new__(cls)
        return cls._instance

    @handle_error
    def getDepartment():
        deptCode = request.args.get('deptCode')
        if deptCode:
            department = Department.query.filter_by(deptCode=deptCode).first()
            students = list(map(Student.as_dict, department.students))
            return jsonify(success=True, students=students)
        else:
            departments = Department.query.all()
            departments = list(map(Student.as_dict, departments))
            return jsonify(success=True, departments=departments)

    @handle_error
    @schema.validate(departmentSchema)
    def addDepartment():
        deptCode, deptName = request.json.get('deptCode'), request.json.get('deptName')
        department = Department(deptCode=deptCode, deptName=deptName)
        db.session.add(department)
        db.session.commit()
        return jsonify(success=True, student=department.as_dict())

    @handle_error
    def deleteDepartment():
        deptCode = request.args.get('deptCode')
        department = Department.query.filter_by(deptCode=deptCode).first()
        db.session.delete(department)
        db.session.commit()
        return jsonify(success=True)