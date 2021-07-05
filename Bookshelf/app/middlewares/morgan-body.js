const fs = require('fs');

const log = fs.createWriteStream("morganBody.log", { flags: "a" });

const config =  { noColors: true, stream: log }

module.exports = config;