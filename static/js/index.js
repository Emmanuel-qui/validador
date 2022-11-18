$(document).ready(function () {
  var url = "http://127.0.0.1:8000/profile/user/";

  $.get(url, function (response) {
    $("#user_email").html(response.email);
    $("#user_email_p").html(response.email);
    $("#user_empresa_h5").html(response.name);
  });
});

var menu = document.getElementById("menu");

menu.addEventListener("click", function () {
  var barra = document.getElementById("sidebar");
  barra.style.left = "0";
});
var cerrar = document.getElementById("cerrar");
cerrar.addEventListener("click", function () {
  var barra = document.getElementById("sidebar");
  barra.style.left = "-270px";
});

function actual() {
  fecha = new Date(); //Actualizar fecha.
  hora = fecha.getHours(); //hora actual
  minuto = fecha.getMinutes(); //minuto actual
  segundo = fecha.getSeconds(); //segundo actual
  if (hora < 10) {
    //dos cifras para la hora
    hora = "0" + hora;
  }
  if (minuto < 10) {
    //dos cifras para el minuto
    minuto = "0" + minuto;
  }
  if (segundo < 10) {
    //dos cifras para el segundo
    segundo = "0" + segundo;
  }
  //devolver los datos:
  mireloj = hora + " : " + minuto + " : " + segundo;
  return mireloj;
}

function actualizar() {
  //función del temporizador
  mihora = actual(); //recoger hora actual
  mireloj = document.getElementById("date"); //buscar elemento reloj
  mireloj.innerHTML = mihora; //incluir hora en elemento
}
setInterval(actualizar, 1000); //iniciar temporizador
