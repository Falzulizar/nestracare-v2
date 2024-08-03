document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");
    const registerLink = document.getElementById("register-link");
    const loginLink = document.getElementById("login-link");
    const loginLink2 = document.getElementById("login-link-2");

    registerLink.addEventListener("click", function(event) {
      event.preventDefault();
      loginForm.style.display = "none";
      registerForm.style.display = "block";
    });

    loginLink.addEventListener("click", function(event) {
      event.preventDefault();
      loginForm.style.display = "block";
      registerForm.style.display = "none";
    });

    loginLink2.addEventListener("click", function(event) {
      event.preventDefault();
      loginForm.style.display = "block";
      registerForm.style.display = "none";
    });
  });