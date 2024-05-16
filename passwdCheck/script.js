const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');
let attempts = 3;

loginForm.addEventListener('submit', (event) => {
    event.preventDefault();
    let hasUsernameError = false;
    let hasPasswordError = false;

    // Username Validation
    if (!validateUsername(usernameInput.value)) {
        usernameError.textContent = "• Invalid username. Please enter a valid email address.";
        hasUsernameError = true;
    } else {
        usernameError.textContent = "";
    }

    // Password Validation
    const passwordErrors = validatePassword(passwordInput.value);
    if (passwordErrors.length > 0) {
        const formattedErrors = passwordErrors.map(error => `• ${error}`).join('\n\n');
        passwordError.textContent = formattedErrors;
        hasPasswordError = true;
    } else {
        passwordError.textContent = "";
    }

    // Check for errors and attempts
    if (hasUsernameError || hasPasswordError) {
        attempts--;
        if (attempts === 0) {
            alert("No more chances. Please try again later.");
            usernameInput.disabled = true;
            passwordInput.disabled = true;
        } else {
            alert(`You have ${attempts} attempts remaining.`);
        }
    } else {
        // Successful Login (replace with your login logic)
        alert("Login Successful!");
        // Clear form for next attempt (optional)
        usernameInput.value = "";
        passwordInput.value = "";
        attempts = 3; // Reset attempts for next login
    }
});

function validateUsername(username) {
    const emailRegex = /^\[^\\s@\]+@\[^\\s@\]+\\.\[^\\s@\]+$/;
    return emailRegex.test(username);
}

function validatePassword(password) {
    const errors = [];
    if (password.length < 8) {
        errors.push("Password must be at least 8 characters long");
    }
    if (!/\[a-z\]/.test(password)) {
        errors.push("Password must contain lowercase letters");
    }
    if (!/\[A-Z\]/.test(password)) {
        errors.push("Password must contain uppercase letters");
    }
    if (!/\\d/.test(password)) {
        errors.push("Password must contain at least one number");
    }
    if (!/\[^a-zA-Z0-9\]/.test(password)) {
        errors.push("Password must contain at least one symbol");
    }
    return errors;
}