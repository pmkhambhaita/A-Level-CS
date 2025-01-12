var redLight = document.getElementById('red');
var yellowLight = document.getElementById('yellow');
var greenLight = document.getElementById('green');
var currentLight = 'red';
var intervalId;
var timeoutId;

function resetLights() {
    redLight.style.background = 'red';
    yellowLight.style.background = 'white';
    greenLight.style.background = 'white';
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

resetLights();

function changeLight() {
    resetLights();

    redLight.style.background = 'red';
    yellowLight.style.background = 'yellow';

    sleep(2000).then(() => {
        redLight.style.background = 'white';
        yellowLight.style.background = 'white';
        greenLight.style.background = 'green';
    });

    sleep(6000).then(() => {
        greenLight.style.background = 'white';
        yellowLight.style.background = 'yellow';
    });

    sleep(8000).then(() => {
        yellowLight.style.background = 'white';
        redLight.style.background = 'red';
    });

}


document.getElementById('button').addEventListener('click', changeLight);