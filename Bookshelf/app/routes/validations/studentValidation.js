var { Validator } = require('express-json-validator-middleware');

const validate = new Validator({allErrors: true}).validate;

const StudentSchema = {
    type: 'object',
    required: ['rNo', 'firstName', 'lastName', 'dept'],
    properties: {
        rNo: {
            type: 'string'
        },
        firstName: {
            type: 'string'
        },
        lastName: {
            type: 'string'
        },
        dept: {
            type: 'string'
        }
    }
}

const StudentValidate = validate({body: StudentSchema});

module.exports = StudentValidate;