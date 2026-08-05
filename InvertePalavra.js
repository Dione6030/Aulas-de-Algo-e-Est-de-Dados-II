const prompt = require('prompt-sync')();

const palavra = prompt("Digite uma palavra: ")

const soletra = palavra.split("")

for(let i = soletra.length -1; i >= 0; i--){
    console.log(soletra[i])
}