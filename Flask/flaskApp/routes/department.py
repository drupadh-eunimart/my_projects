from flaskApp import app, db
from flaskApp.services.department import DepartmentServices

services = DepartmentServices

app.add_url_rule("/departments", view_func=services.getDepartment, methods=['GET'])

app.add_url_rule("/departments", view_func=services.addDepartment, methods=['POST'])

app.add_url_rule("/departments", view_func=services.deleteDepartment, methods=['DELETE'])
