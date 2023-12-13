document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('inicio_sesion'), {
        backdrop: 'static',
        keyboard: false
    });
    myModal.show();
});
