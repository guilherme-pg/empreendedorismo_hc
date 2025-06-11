  let html5QrCode;

  function startScanner() {
    document.getElementById("scanner-modal").style.display = "flex";
    html5QrCode = new Html5Qrcode("reader");
    const config = { fps: 10, qrbox: 250 };

    html5QrCode.start(
      { facingMode: "environment" },
      config,
      qrCodeMessage => {
        fetch("/registrar_presenca", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ qrcode: qrCodeMessage })
        })
        .then(res => res.json())
        .then(data => {
          alert(data.message);
          stopScanner();
        });
      }
    ).catch(err => {
      alert("Erro ao iniciar a câmera.");
      console.error(err);
      stopScanner();
    });
  }

  function stopScanner() {
    if (html5QrCode) {
      html5QrCode.stop().then(() => {
        html5QrCode.clear();
        document.getElementById("scanner-modal").style.display = "none";
      }).catch(err => {
        console.error("Erro ao parar o scanner", err);
        document.getElementById("scanner-modal").style.display = "none";
      });
    } else {
      document.getElementById("scanner-modal").style.display = "none";
    }
  }
