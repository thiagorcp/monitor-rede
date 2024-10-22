document.getElementById('playButton').addEventListener('click', function () {
  const alarme = document.getElementById('alarme');
  alarme.currentTime = 0; // Recomeçar do início
  alarme.play(); // Reproduzir o áudio
});
