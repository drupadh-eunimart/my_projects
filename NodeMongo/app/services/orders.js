const Order = require('../models/order');

class OrderServices {

    getOrders = async (req, res) => {
        try{
            const orders = await Order.find({});
            res.json({success:true, orders})
        }catch(error){
            // console.log(error)
            res.json({success:false, error})
        }
    }

    getOrder = async (req,res) => {
        try{
            const orderId = req.query.orderId
            if(!orderId) {
                return this.getOrders(req,res)
            }
            const order = await Order.findOne({orderId});
            res.json({success:true, order})
        }catch(error){
            res.json({success:false, error})
        }
    }

    addOrder = async (req,res) => {
        try{
            const {orderId, buyerName, mobile, email, products} = req.body;
            const order = new Order({orderId, buyerName, mobile, email, products});
            await order.save()
            res.json({success:true, order})
        }catch(error){
            res.json({success:false, error})
        }
    }

    deleteOrder = async (req,res) => {
        try{
            const orderId = req.query.orderId
            await Order.findOneAndDelete({orderId})
            res.json({success:true})
        }catch(error){
            res.json({success:false, error})
        }
    }

    updateOrder = async (req,res) => {
        try{
            const orderId = req.query.orderId
            const products = req.body.products
            const order = await Order.findOneAndUpdate({orderId}, {products}, {new:true})
            res.json({success:true, order})
        }catch(error){
            res.json({success:false, error})
        }
    }
}

module.exports = new OrderServices();