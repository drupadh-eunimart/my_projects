const bookshelf = require('../utils/db');
// const Department = require('./department');

// Defining models
const Student = bookshelf.model('Student', {
    tableName: 'STUDENTS',
    department() {
        return this.belongsTo('Department');
    }
})

module.exports = Student;