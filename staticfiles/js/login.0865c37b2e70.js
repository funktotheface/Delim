//this script prevents users from pressing the login button while the csrf token is being handled, whioch can cause a 403 error

document.addEventListener('DOMContentLoaded', () => {
    console.log('login.js loaded'); 
   

    const loginButton = document.getElementById('login-btn');
    const loginForm = document.getElementById('login-form'); // Assuming your form has an ID of 'login-form'

    if (loginButton && loginForm) {
        loginForm.addEventListener('submit', () => {
            loginButton.disabled = true; // Disable button on form submission
        });

        setTimeout(() => {
            loginButton.disabled = false; // Allow button press after autofill completes
        }, 1000); // Adjust delay as needed
    } else {
        console.error('login-btn or login-form element not found');
    }
});