const express = require('express');
const router = express.Router();
const DepartmentServices = require('../services/departments');

router
    .route('/')
    .get(DepartmentServices.getAllDepartments)
    .post(DepartmentServices.addDepartment);

router
    .route('/:deptCode')
    .get(DepartmentServices.getDepartment)

module.exports = router;