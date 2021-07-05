const express = require('express');
const router = express.Router();
const OrderServices = require('../services/orders');

router
    .route('/')
    .get(OrderServices.getOrder)
    .post(OrderServices.addOrder)
    .delete(OrderServices.deleteOrder)
    .patch(OrderServices.updateOrder);

module.exports = router;