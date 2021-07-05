from flaskApp import db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deptCode = db.Column(db.String(55), unique=True, nullable=False)
    deptName = db.Column(db.String(255), nullable=False)
    students = db.relationship('Student', cascade="all, delete", backref='department', lazy=True)

    def __repr__(self):
        return f"Department('{self.id}', '{self.deptCode}', '{self.deptName}')"
    
    def as_dict(self):
       return {column.name: getattr(self, column.name) for column in self.__table__.columns}