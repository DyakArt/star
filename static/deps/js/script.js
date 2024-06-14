document.addEventListener("DOMContentLoaded", function() {
  var buttons = document.querySelectorAll(".respond");
  var modal = document.getElementById('modal');
  var closeModal = document.getElementsByClassName('close')[0];

  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      modal.style.display = "block";
    });
  });

  closeModal.onclick = function() {
    modal.style.display = "none";
  }

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
});
