$(document).ready(function(){
    var url = 'http://127.0.0.1:8000/profile/user/';

    $.get(url, function(response){
        $("#user_email").html(response.email);
        $("#user_email_p").html(response.email);
        
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
