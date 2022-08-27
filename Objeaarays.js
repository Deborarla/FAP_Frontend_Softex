var fiat ={
    modelo: 'Palio',
    ano: 2012,
    fabricacao: 2013,
    direcao: 'Hidráulica'
}

var marcas = ['Carro', 'Bicicleta', 'Moto', 'Avião', 'Navio']

function loop(cont){
    for(var cont = 0; cont <= 3; cont++){
        console.log(marcas[cont])
    }
}
function obj(){
    console.log(fiat)
}
console.log(obj())
console.log(loop())