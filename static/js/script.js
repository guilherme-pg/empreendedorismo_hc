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


function abrirLeitorQR() {
  document.getElementById("qr-modal").style.display = "block";

  const html5QrCode = new Html5Qrcode("qr-reader");
  html5QrCode.start(
    { facingMode: "environment" },
    {
      fps: 10,
      qrbox: 250
    },
    (decodedText) => {
      html5QrCode.stop();
      fetch('/registrar_presenca', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ qrcode: decodedText })
      })
      .then(res => res.json())
      .then(data => {
        alert(data.mensagem);
        fecharQR();
      });
    },
    (errorMessage) => {}
  );
}

function fecharQR() {
  document.getElementById("qr-modal").style.display = "none";
  document.getElementById("qr-reader").innerHTML = ""; // Reset scanner
}