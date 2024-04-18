var redLight = document.getElementById('red');
var yellowLight = document.getElementById('yellow');
var greenLight = document.getElementById('green');
var currentLight = 'red';
var intervalId;

function changeLight() {
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

document.getElementById('button').addEventListener('click', function() {
    if (intervalId) {
        clearInterval(intervalId); // stop the current cycle if it's running
    }
    intervalId = setInterval(changeLight, 1000); // start a new cycle
});