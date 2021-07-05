from flaskApp import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rNo = db.Column(db.String(55), unique=True, nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), db.ForeignKey('department.deptCode'), nullable=False)


    def __repr__(self):
        return f"Student('{self.id}', '{self.rNo}', '{self.firstName}', '{self.lastName}', '{self.dept}')"
    
    def as_dict(self):
       return {column.name: getattr(self, column.name) for column in self.__table__.columns}