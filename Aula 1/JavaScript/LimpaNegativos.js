const numeros = [-5,-4,-3,-2,-1,0,1,2,3,4,5]

const positivos = []

for(let i = 0; i <= numeros.length; ++i){
    if(numeros[i] >= 0){
        positivos.push(numeros[i])
    }
}

console.log(positivos[0], positivos[1], positivos[2], positivos[3])