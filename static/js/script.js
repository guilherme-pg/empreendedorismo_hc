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

  const msgBtn = document.getElementById('msg-btn');
  const notiBtn = document.getElementById('noti-btn');
  const msgPopup = document.getElementById('msg-popup');
  const notiPopup = document.getElementById('noti-popup');

  // Função para fechar todos os popups
  function closeAllPopups() {
    msgPopup.style.display = 'none';
    notiPopup.style.display = 'none';
  }

  msgBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (msgPopup.style.display === 'block') {
      msgPopup.style.display = 'none';
    } else {
      closeAllPopups();
      msgPopup.style.display = 'block';
    }
  });

  notiBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (notiPopup.style.display === 'block') {
      notiPopup.style.display = 'none';
    } else {
      closeAllPopups();
      notiPopup.style.display = 'block';
    }
  });

  // Fechar com o botão de fechar
  document.querySelectorAll('.close-popup').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetId = btn.getAttribute('data-target');
      document.getElementById(targetId).style.display = 'none';
    });
  });

  // Fechar popups ao clicar fora
  document.addEventListener('click', () => {
    closeAllPopups();
  });

  // Evitar fechar ao clicar dentro da popup
  [msgPopup, notiPopup].forEach(popup => {
    popup.addEventListener('click', e => {
      e.stopPropagation();
    });
  });