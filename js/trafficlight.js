var redLight = document.getElementById('red');
var yellowLight = document.getElementById('yellow');
var greenLight = document.getElementById('green');
var currentLight = 'red';
var intervalId;
var timeoutId;

function resetLights() {
    redLight.style.background = 'white';
    yellowLight.style.background = 'white';
    greenLight.style.background = 'white';
}

function changeLight() {
    resetLights();

    if (currentLight === 'red') {
        redLight.style.background = 'red';
        yellowLight.style.background = 'yellow';
        currentLight = 'red-yellow';
    } else if (currentLight === 'red-yellow') {
        yellowLight.style.background = 'yellow';
        greenLight.style.background = 'green';
        currentLight = 'green';
    } else if (currentLight === 'green') {
        yellowLight.style.background = 'yellow';
        currentLight = 'yellow';
    } else {
        redLight.style.background = 'red';
        currentLight = 'red';
    }
}

function startCycle() {
    if (intervalId) {
        clearInterval(intervalId); // stop the current cycle if it's running
    }
    if (timeoutId) {
        clearTimeout(timeoutId); // stop the current timeout if it's running
    }
    intervalId = setInterval(changeLight, 1000); // start a new cycle
    timeoutId = setTimeout(function() {
        clearInterval(intervalId); // stop the cycle after 4 seconds (1 second per light)
        resetLights();
        redLight.style.background = 'red'; // return to red
    }, 4000);
}

document.getElementById('button').addEventListener('click', startCycle);