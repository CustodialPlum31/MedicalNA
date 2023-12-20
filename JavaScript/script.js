document.addEventListener('DOMContentLoaded', function() {
    var myCarousel = new bootstrap.Carousel(document.getElementById('myCarousel'), {
      interval: 4000, // Intervalo en milisegundos (4 segundos en este caso)
      pause: false // No pausa en el hover
    });
  });