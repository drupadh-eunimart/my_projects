const express = require('express');
const app = express();
const students = require('./app/routes/students');
const departments = require('./app/routes/departments');

app.use(express.urlencoded({ extended: true }));


// const requestResponseLogger = require('./app/middlewares/logger')
// app.use(requestResponseLogger);

// const morganBody = require('morgan-body')
// const morganBodyConfig = require('./app/middlewares/morgan-body')
// morganBody(app, morganBodyConfig)

app.use((req,res,next)=>{
    res.on('finsih', ()=>{
        console.log(res.statusCode)
    })
    next()
})

app.use("/students", students);

app.use("/departments", departments); //not yet completed


app.listen(3000, () => {
    console.log("LISTENING ON PORT:3000!")
})