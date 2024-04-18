// var products = ['Printer', 'Tablet','Router']
// products.sort();
// console.log(products);
// console.log(products.length);

var currentLight = 'red';

function changeLight() {
    var redLight = document.getElementById('red');
    var yellowLight = document.getElementById('yellow');
    var greenLight = document.getElementById('green');

    redLight.style.background = 'white';
    yellowLight.style.background = 'white';
    greenLight.style.background = 'white';

    if (currentLight === 'red') {
        yellowLight.style.background = 'yellow';
        currentLight = 'yellow';
    } else if (currentLight === 'yellow') {
        greenLight.style.background = 'green';
        currentLight = 'green';
    } else {
        redLight.style.background = 'red';
        currentLight = 'red';
    }
}