document.addEventListener("DOMContentLoaded", function() {
    const questions = document.querySelectorAll('.question');
  
    questions.forEach(question => {
      question.addEventListener('click', function() {
        const answer = this.nextElementSibling;
        const isOpen = answer.classList.contains('show');
        const openAnswer = document.querySelector('.answer.show');
        
        if (openAnswer && openAnswer !== answer) {
          openAnswer.classList.remove('show');
        }
  
        if (!isOpen) {
          answer.classList.add('show');
        } else {
          answer.classList.remove('show');
        }
      });
    });
  });
  
const hamburger = document.querySelector('.hamburger');
const navUl = document.querySelector('nav ul');

hamburger.addEventListener('click', () => {
    navUl.classList.toggle('show');
});

window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        navUl.classList.remove('show');
    }
});
