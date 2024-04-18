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

function startCycle() {
    if (intervalId) {
        clearInterval(intervalId); // stop the current cycle if it's running
    }
    if (timeoutId) {
        clearTimeout(timeoutId); // stop the current timeout if it's running
    }
    intervalId = setInterval(changeLight, 1000); // start a new cycle
    timeoutId = setTimeout(function() {
        clearInterval(intervalId); // stop the cycle after 3 seconds (1 second per light)
        resetLights();
        redLight.style.background = 'red'; // return to red
    }, 3000);
}

document.getElementById('button').addEventListener('click', startCycle);