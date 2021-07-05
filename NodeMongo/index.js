const express = require('express');
const app = express();
const mongoose = require('mongoose');
const orders = require('./app/routes/orders');

app.use(express.json());

mongoose.connect('mongodb://localhost:27017/nodeMongoDb', { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true})
.then(() => {
    console.log("DB CONNECTED SUCCESSFULLY")
})
.catch(err => {
    console.log("DB CONNECTED FAILED!!!")
    console.log(err)
})

app.use('/orders', orders);

app.listen(3000, () => {
    console.log("LISTENING ON PORT:3000!")
})