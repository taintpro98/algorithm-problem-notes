// let str = "<div><b><p>hello world</p></b></div>";
// const elements = str.match(/<\/?[^>]*>/g) || [];
// console.log(elements)

// let text = "The rain in SPAIN stays mainly in the plain";
// const a = text.match(/ain/);
// console.log(a)

const str = '<div><b><p>hello world</p></b></div>';
const elements = str.match(/<\/?[^>]*>/g) || [];
console.log(elements)