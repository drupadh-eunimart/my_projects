const Order = require('../models/order');

class OrderServices {
    getOrder = async (req,res) => {
        try{
            const order_id = req.query.order_id
            const order = await Order.findOne({order_id});
            if(order){
                res.json({success:true, order})
            }else{
                throw Error("No orders found!!!")
            }
        }catch(error){
            res.json({success:false, error})
            console.log(error)
        }
    }

    postOrder = async (req,res) => {
        try{
            const {order_id, name, email, ordered, total_amount, payment_type, products} = req.body;
            const order = new Order({order_id, name, email, ordered, total_amount, payment_type, products});
            await order.save()
            res.json({success:true, order})
        }catch(error){
            res.json({success:false, error})
        }
    }
}

module.exports = new OrderServices();