const prompt = require('prompt-sync')();

const palavra = prompt("Digite uma palavra: ")

const soletra = palavra.split("")

for (let i = 0; i <= palavra.length; i++){
    console.log("*")
}
