  let scanner = null;

  function startScanner() {
    document.getElementById("scanner-modal").style.display = "flex";

    scanner = new Html5Qrcode("reader");

    const config = {
      fps: 10,
      qrbox: { width: 250, height: 250 }
    };

    scanner.start(
      { facingMode: "environment" },
      config,
      qrCodeMessage => {
        alert("QR Code detectado: " + qrCodeMessage);
        stopScanner();
      },
      errorMessage => {
        console.log("Erro de leitura:", errorMessage);
      }
    ).catch(err => {
      console.error("Erro ao iniciar scanner:", err);
    });
  }

  function stopScanner() {
    if (scanner) {
      scanner.stop().then(() => {
        scanner.clear();
        scanner = null;
        document.getElementById("scanner-modal").style.display = "none";
      }).catch(err => {
        console.error("Erro ao parar o scanner:", err);
      });
    } else {
      document.getElementById("scanner-modal").style.display = "none";
    }
  }
