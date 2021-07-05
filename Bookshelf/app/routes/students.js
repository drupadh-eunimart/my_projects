const express = require('express');
const router = express.Router();
const StudentServices = require('../services/students');
const ValidateError = require('../middlewares/validationError');
const StudentValidate = require('./validations/studentValidation');

router
    .route('/')
    .get(StudentServices.getStudent)
    .post(StudentValidate, StudentServices.addStudent)
    .delete(StudentServices.deleteStudent)
    .patch(StudentServices.updateStudent);

router.use(ValidateError);

module.exports = router;