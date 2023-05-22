let oiMundo = "SALVE MEU NOBRE";

let olaMundo = 'SALVE MEU BOM';

let concatenar = oiMundo + olaMundo;
console.log("primeiro: " + concatenar);

let salve = oiMundo.concat(olaMundo);
console.log("segundo: "  + salve);

let nobre = oiMundo.concat("MEU CONSAGRADO", olaMundo, "É NOIS");
console.log(nobre);

let templeate = `${olaMundo} ${oiMundo} ${2+2}`;
console.log(templeate);

// Caracteres Especiais
// \n: nova linha
// \\: mostra \
// \': mostra '
// \": mostra "
let CaracteresEspeciais = "Lorem \n Ipsun \\ Dolor \'\" Amet";
console.log(CaracteresEspeciais);