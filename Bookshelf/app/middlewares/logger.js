const logger = require('../utils/winstonLogger');

const requestResponseLogger = (req,res,next)=>{
    logger.info(req.body);
    let send = res.send;
    res.send = function(data){
        logger.info(JSON.parse(data))
        // arguments[0] = arguments[0].slice(0,-1)+',"author":"drupadh"}'
        arguments[0] = JSON.stringify({...JSON.parse(arguments[0]), author:"drupadh"})
        send.apply(res, arguments)
    }
    next();
}

module.exports = requestResponseLogger;