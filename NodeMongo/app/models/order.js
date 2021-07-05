const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
    orderId: {
        type: Number,
        unique: true,
        required: [true, 'Order Id required!!!']
    },
    buyerName: {
        type: String,
        required: [true, "Buyer's Name required!!!"]
    },
    mobile: {
        type: Number,
        required: [true, "Mobile Number required!!!"]
    },
    email: {
        type: String,
        required: [true, "Email Id required!!!"]
    },
    products: [
        {
            productId: {
                type: Number,
                required: [true, "Products required!!!"]
            }
        }
    ]
})

module.exports = mongoose.model('Order', orderSchema);