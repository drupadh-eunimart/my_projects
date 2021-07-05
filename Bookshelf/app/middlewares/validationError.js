const { ValidationError } = require("express-json-validator-middleware");

const ValidateError = (err, req, res, next)=>{
        if (err instanceof ValidationError) {
            res.json({success:false, err});
            return next();
        }
        return next(err);
    }

module.exports = ValidateError;