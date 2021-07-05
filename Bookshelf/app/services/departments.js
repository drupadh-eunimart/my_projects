const Department = require('../models/department');

class DepartmentServices {
    getAllDepartments(req,res) {
        Department.fetchAll()
        .then((departments)=>{
            res.json({success:true, departments})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }

    getDepartment(req,res) {
        const {deptCode} = req.params
        Department.where({deptCode}).fetch({withRelated: ['students']})
        .then((department) => {
            res.json({success:true, department})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }

    addDepartment(req,res) {
        const { deptCode, deptName } = req.body
        new Department({deptCode, deptName}).save()
        .then((department)=>{
            res.json({success:true, department:department.toJSON()})
        })
        .catch((e)=>{
            res.json({success:false, err:e})
        })
    }
}

module.exports = new DepartmentServices();