const fs= require('fs');

fs.readFile('./pessoas.json', 'utf-8', (error, data)=>{
  
if(error){
    console.log(error);
    return;
}

    try{
  const pessoas=  JSON.parse(data);
    console.log(pessoas.nome);
    }catch (e) {
        console.log(e);
    }
})