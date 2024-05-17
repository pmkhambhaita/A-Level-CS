const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');
const attemptsLeftSpan = document.getElementById('attemptsLeft');
const errorMessage = document.getElementById('errorMessage');
const retryButton = document.getElementById('retryButton');

let attemptsLeft = 3;

const passwordRequirements = {
  minLength: 8,
  hasUpperCase: false,
  hasLowerCase: false,
  hasNumber: false,
  hasSymbol: false,
};

const togglePasswordVisibility = () => {
  const passwordField = document.getElementById('password');
  const eyeIcon = document.querySelector('.password-toggle');
  if (passwordField.type === 'password') {
    passwordField.type = 'text';
    eyeIcon.classList.remove('fa-eye-slash');
    eyeIcon.classList.add('fa-eye');
  } else {
    passwordField.type = 'password';
    eyeIcon.classList.remove('fa-eye');
    eyeIcon.classList.add('fa-eye-slash');
  }
};

const validateUsername = (username) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(username);
};

const validatePassword = (password) => {
  passwordRequirements.hasUpperCase = /[A-Z]/.test(password);
  passwordRequirements.hasLowerCase = /[a-z]/.test(password);
  passwordRequirements.hasNumber = /\d/.test(password);
  passwordRequirements.hasSymbol = /[^\w\s]/.test(password);

  const errors = [];
  if (password.length < passwordRequirements.minLength) {
    errors.push(`Minimum ${passwordRequirements.minLength} characters`);
  }
  if (!passwordRequirements.hasUpperCase) {
    errors.push('At least one uppercase letter');
  }
  if (!passwordRequirements.hasLowerCase) {
    errors.push('At least one lowercase letter');
  }
  if (!passwordRequirements.hasNumber) {
    errors.push('At least one number');
  }
  if (!passwordRequirements.hasSymbol) {
    errors.push('At least one symbol');
  }
  return errors;
};

const updatePasswordRequirements = () => {
  const passwordReqElements = document.querySelectorAll('.password-requirements span');
  passwordReqElements.forEach((element) => {
    if (passwordRequirements[element.classList[1]]) {
      element.classList.remove('req-not-met');
      element.classList.add('req-met');
    } else {
      element.classList.remove('req-met');
      element.classList.add('req-not-met');
    }
  });
};

const handleFormSubmission = (event) => {
  event.preventDefault();

  usernameError.textContent = '';
  passwordError.textContent = '';
  errorMessage.textContent = '';

  const username = usernameInput.value;
  const password = passwordInput.value;

  if (!validateUsername(username)) {
    usernameError.textContent = 'Invalid username. Please enter a valid email address.';
    return;
  }

  const passwordErrors = validatePassword(password);
  if (passwordErrors.length > 0) {
    passwordError.textContent = 'Password is weak: ' + passwordErrors.join(', ');
    updatePasswordRequirements();
    return;
  }

  // Successful login logic (replace with your actual login logic)
  alert('Login Successful!');

  // Clear form for next attempt (optional)
  usernameInput.value = '';
  passwordInput.value = '';
  attemptsLeft = 3;
  attemptsLeftSpan.textContent = attemptsLeft;
  errorMessage.textContent = '';
  retryButton.disabled = true;
};

constloginForm.addEventListener('submit', handleFormSubmission);

const passwordToggle = document.querySelector('.password-toggle');
passwordToggle.addEventListener('click', togglePasswordVisibility);

retryButton.addEventListener('click', () => {
  attemptsLeft = 3;
  attemptsLeftSpan.textContent = attemptsLeft;
  errorMessage.textContent = '';
  usernameError.textContent = '';
  passwordError.textContent = '';
  retryButton.disabled = true;
  updatePasswordRequirements();
});
