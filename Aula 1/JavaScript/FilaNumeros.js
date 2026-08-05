const prompt = require('prompt-sync')()

const fila = ["Carlos", "Rodrigo", "Pedro", "Paulo", "Diego"]

const novaFila = []

console.log("Fila Atualmente")
console.log(fila)

const NovoIntegrante = prompt("Digite o nome do novo Integrante: ")

for(let i = 1; i < fila.length; i++){
    if(i > 0){
        novaFila.push(fila[i])
    }
}

novaFila.push(NovoIntegrante)

console.log("Fila Atualmente")
console.log(novaFila)
