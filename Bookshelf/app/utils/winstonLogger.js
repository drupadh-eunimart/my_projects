const winston = require('winston');

const logger = winston.createLogger({
    transports: [
      new winston.transports.File({ filename: 'reqRes.log' })
    ]
  });

module.exports = logger;