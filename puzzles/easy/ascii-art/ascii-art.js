//the standard input according to the problem statement.

const L = parseInt(readline());
const H = parseInt(readline());
const T = readline();

for (let i = 0; i < H; i++) {
    const ROW = readline();
    let outLog = "";
    for (let i = 0; i < T.length; i++) {
        ch = T[i].toUpperCase().charCodeAt(0)
        let index = 26
        if (ch >= 65 && ch <= 91) {
            index = ch - 65
        }
        outLog += ROW.slice(index * L, (index + 1) * L);
    }
    console.log(outLog);
}
