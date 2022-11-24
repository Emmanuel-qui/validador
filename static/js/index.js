

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
