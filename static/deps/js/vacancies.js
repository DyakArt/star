document.addEventListener("DOMContentLoaded", function() {
  //код для модального окна
  let buttons = document.querySelectorAll(".respond");
  let modal = document.getElementById('modal');
  let closeModal = document.getElementsByClassName('close')[0];

  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      modal.style.display = "block";
    });
  });

  closeModal.onclick = function() {
    modal.style.display = "none";
  }

  window.onclick = function(event) {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  }
});