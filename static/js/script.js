document.addEventListener("DOMContentLoaded", function () {
    const errorMessage = document.body.dataset.errorMessage;

    if (errorMessage) {
        Swal.fire({
            icon: 'error',
            title: 'Erro de Autenticação',
            text: errorMessage,
        });
    }
});
