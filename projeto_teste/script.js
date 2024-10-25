document.getElementById('Button-alarm').addEventListener('click', function () {
  const alarme = document.getElementById('alarme');
  alarme.currentTime = 0; // Recomeçar do início
  alarme.play(); // Reproduzir o áudio
});

document.getElementById('Button-semi-return').addEventListener('click', function () {
  const alarme = document.getElementById('semi-volta');
  alarme.currentTime = 0; // Recomeçar do início
  alarme.play(); // Reproduzir o áudio
});

document.getElementById('Button-return').addEventListener('click', function () {
  const alarme = document.getElementById('volta');
  alarme.currentTime = 0; // Recomeçar do início
  alarme.play(); // Reproduzir o áudio
});

document.getElementById('Button-sintrama').addEventListener('click', function () {
  const alarme = document.getElementById('sintrama');
  alarme.currentTime = 0; // Recomeçar do início
  alarme.play(); // Reproduzir o áudio
});
