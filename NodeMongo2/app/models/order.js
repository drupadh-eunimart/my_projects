const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({

    order_id: { type: Number, unique: true, required: true },
    
    name: { type: String, required: true },
    
    email: { type: String, required: true },
    
    ordered: { type: Date, default: Date.now },
    
    total_amount: { type: Number, required: true },
    
    payment_type: { type: String, required: true },

    products: [
        {
            name: { type: String, required: true},
            price: { type: Number, required: true},
            quantity: { type: Number, required: true},
            item_total: { type: Number, required: true},
        }
    ]
})

module.exports = mongoose.model('Order', orderSchema);