// the standard input according to the problem statement.
const n = parseInt(readline()); // the number of temperatures to analyse
if (n == 0) {
    console.log(0)
    process.exit()
}
var listT = readline().split(' ');
var minT = 5526
for (let i = 0; i < n; i++) {
    const t = parseInt(listT[i]);// a temperature expressed as an integer ranging from -273 to 5526
    let abs_t = Math.abs(t);
    if (abs_t < minT) {
        minT = abs_t;
    }
}
if (listT.includes(String(minT))) {
    console.log(minT);
} else {
    console.log(-minT);
}
