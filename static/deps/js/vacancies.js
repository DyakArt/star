document.addEventListener("DOMContentLoaded", function() {
  //код для модального окна
  let buttons = document.querySelectorAll(".respond");
  let modal = document.getElementById('modal');
  let closeModal = document.getElementsByClassName('close')[0];
  let modalJobTitle = document.getElementById('modal-job-title');

  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      // Устанавливаем название должности в модальное окно
      modalJobTitle.textContent = this.getAttribute('data-title');

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