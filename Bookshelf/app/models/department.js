const bookshelf = require('../utils/db');
// const Student = require('./student');

// Defining models
const Department = bookshelf.model('Department', {
    tableName: 'DEPARTMENTS',
    students() {
        return this.hasMany('Student')
    }
})

module.exports = Department;