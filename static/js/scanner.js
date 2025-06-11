let html5QrCode;

function startScanner() {
  document.getElementById("reader").style.display = "block";
  html5QrCode = new Html5Qrcode("reader");
  const config = { fps: 10, qrbox: 250 };

  html5QrCode.start(
    { facingMode: "environment" },
    config,
    qrCodeMessage => {
      document.getElementById("result").innerText = `Código detectado: ${qrCodeMessage}`;
      fetch("/registrar_presenca", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ qrcode: qrCodeMessage })
      }).then(res => res.json()).then(data => {
        alert(data.message);
        stopScanner();
      });
    }
  );
}

function stopScanner() {
  if (html5QrCode) {
    html5QrCode.stop().then(() => {
      html5QrCode.clear();
      document.getElementById("reader").style.display = "none";
    });
  }
}
