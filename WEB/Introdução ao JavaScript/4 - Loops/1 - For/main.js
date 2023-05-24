for(let i = 0; i < 11; i++){
    console.log(i);
}

console.log("=======================================")


let lista = ["doginho", "gatinho", "xurasxkeira", "sorvete", "amendolangos"];
for(let a = 0; a < lista.length; a++){
    console.log(lista[a]);
}

console.log("=======================================")

let vetores = [1,2,3,4,5,6,7,8,9];
for (let y = 0; y < vetores.length; y++){
    vetores[y] = vetores[y] * 2;
    console.log(vetores[y]);
}

console.log("=======================================")

let b = 5;
for(; b < 16; b++){
    console.log(b);
}

console.log("=======================================")

let w = 0;
for(; w < 10; w++){
    console.log(w);
    w += 2;
}

console.log("=======================================")
let x = 0;
let z = 3;
for (;;){
    console.log(z);
    z += 2;
    x = z/2;
    if (x > 20){
        break;
    }
}