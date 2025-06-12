const freqCtx = document.getElementById('frequenciaChart').getContext('2d');
const avalCtx = document.getElementById('avaliacoesChart').getContext('2d');
const horasCtx = document.getElementById('horasChart').getContext('2d');

new Chart(freqCtx, {
  type: 'bar',
  data: {
    labels: ['Claudio', 'Carla', 'Lucas', 'Fernanda', 'João'],
    datasets: [{
      label: 'Dias Presentes (Abril)',
      data: [18, 20, 17, 15, 19],
      backgroundColor: '#0a66c2'
    }]
  }
});

new Chart(avalCtx, {
  type: 'radar',
  data: {
    labels: ['Comunicação', 'Técnica', 'Pontualidade', 'Humanização', 'Liderança'],
    datasets: [{
      label: 'Dr. Claudio',
      data: [8, 9, 7, 8, 9],
      fill: true,
      backgroundColor: 'rgba(0, 102, 204, 0.2)',
      borderColor: '#003366',
    }]
  }
});

new Chart(horasCtx, {
  type: 'line',
  data: {
    labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril'],
    datasets: [{
      label: 'Dr. João Pedro',
      data: [160, 152, 158, 165],
      borderColor: '#28a745',
      backgroundColor: 'rgba(40, 167, 69, 0.1)',
      fill: true
    }]
  }
});
