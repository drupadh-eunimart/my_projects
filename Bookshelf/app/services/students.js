const Student = require('../models/student');

class StudentServices {
    getAllStudents = (req,res) => {
        Student.fetchAll()
        .then((students)=>{
            res.json({success:true, students})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }

    getStudent = (req,res) => {
        if(!req.query.rNo) {
            return this.getAllStudents(req,res)
        }
        const {rNo} = req.query
        Student.where({rNo}).fetch()
        .then((student) => {
            res.json({success:true, student})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }

    addStudent = (req,res) => {
        const {rNo, firstName, lastName, dept} = req.body
        new Student({rNo, firstName, lastName, dept}).save()
        .then((student)=>{
            res.json({success:true, student:student.toJSON()})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }

    deleteStudent = (req,res) => {
        const {rNo} = req.query
        Student.where({rNo}).destroy()
        .then(()=>{
            res.json({success:true})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }

    updateStudent = (req,res) => {
        const {rNo} = req.query
        const details = req.body
        Student.where({rNo}).save(details, {patch: true})
        .then(()=>{
            res.json({success:true})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }
}


module.exports = new StudentServices();