console.log("============ BREAK")
let n = 0;
while (n < 20){
    console.log("valor: " + n);
    if(n == 10){
        break
    }
    n ++;
}

for(let i = 0; i < 11; i++){
    console.log(i);
    if (i==5){
        break
    }
}
console.log("\n============ CONTINUE")
for(let num of [1,2,3,4,5,6,7,8,9,10]){
    if(num == 3 || num == 8){
        continue;
    }
    console.log(num);
}