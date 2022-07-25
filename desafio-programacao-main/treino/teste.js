const fs = require('fs');

fs.readFile('./pessoas.json'.'utf-8', (error,data)=>{
    console.log(data);
});

