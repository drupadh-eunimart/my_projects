from flaskApp import app
from flaskApp.services.student import StudentServices

services = StudentServices()

app.add_url_rule("/students", view_func=services.getStudent, methods=['GET'])

app.add_url_rule("/students", view_func=services.addStudent, methods=['POST'])

app.add_url_rule("/students", view_func=services.updateStudent, methods=['PATCH'])

app.add_url_rule("/students", view_func=services.deleteStudent, methods=['DELETE'])