document.addEventListener("DOMContentLoaded", function () {
    //код для модального окна
    let buttons_respond = document.querySelectorAll(".btn_rsp");
    let modal = document.getElementById('modal');
    let closeModal = document.getElementsByClassName('close')[0];
    let modalJobTitle = document.getElementById('modal-job-title');
    let submitButton = document.getElementById('button_send');
    let jobTitleInput = document.getElementById('id_job_title');

    buttons_respond.forEach(function (button) {
        button.addEventListener("click", function () {
            // Устанавливаем название должности в модальное окно
            modalJobTitle.textContent = this.getAttribute('data-title');
            jobTitleInput.value = modalJobTitle.textContent;
            modal.style.display = "block";
        });
    });

    closeModal.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }

    modalJobTitle.textContent = jobTitleInput.value;

    if (document.querySelector('.errorlist')) {
        modal.style.display = "block";
    }

    // Код для отображения всплывающего окна с сообщением
    let successModal = document.getElementById('successModal');
    let successClose = document.getElementsByClassName('close-success')[0];

    if (successModal) {
        successModal.style.display = 'block';

        successClose.onclick = function () {
            successModal.style.display = 'none';
        }

        window.onclick = function(event) {
            if (event.target === successModal) {
                successModal.style.display = 'none';
            }
        }
    }
});