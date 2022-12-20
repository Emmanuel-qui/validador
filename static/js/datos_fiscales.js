$(document).ready(function() {
      validate_input();

      select_regimen();
});

function validate_input() {
  
      // validar numero de telefono
      $('#telefono').mask('(000) 000-0000');

      $("#rfc").keyup(function(event) {
          var caracteres = $(this).val().length;

          if(caracteres == 13){
            $(this).keypress(function(event){ return false })
          }
      })


      // validando Codigo Postal.
      $("#postal").keypress(function(event){
        if(event.charCode < 48 || event.charCode > 57){
          return false;
        }
        
      });

      $("#postal").keyup(function(event){

          var caracteres = $(this).val().length;

          if(caracteres == 5){
            $(this).keypress(function(event){ return false })
          }
      });

}

      
function select_regimen(){

     $("#rfc").focus(function(event){
          
          $(this).keyup(function (event){

              var rfc = $(this).val().length;

              if( rfc == 13 ){

                $("#regimen").empty();
                $("#regimen").append("<option selected>Seleccione el regimen fiscal</option>");
                $("#regimen").append("<option value='601'>General de Ley Personas Morales</option>");
                $("#regimen").append("<option value='603'>Personas Morales con Fines no Lucrativos </option>");
                $("#regimen").append("<option value='610'>Residentes en el Extranjero sin Establecimiento Permanente en México</option>");
                $("#regimen").append("<option value='620'>Sociedades Cooperativas de Producción que optan por diferir sus ingresos</option>");
                $("#regimen").append("<option value='622'>Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras</option>");
                $("#regimen").append("<option value='623'>Opcional para Grupos de Sociedades</option>");
                $("#regimen").append("<option value='624'>Coordinados</option>");
                $("#regimen").append("<option value='626'>Régimen Simplificado de Confianza</option>");

              }else {
                $("#regimen").empty();
                $("#regimen").append("<option selected>Seleccione el regimen fiscal</option>");
                $("#regimen").append("<option value='605'>Sueldos y Salarios e Ingresos Asimilados a Salarios</option>");
                $("#regimen").append("<option value='606'>Arrendamiento</option>");
                $("#regimen").append("<option value='607'>Régimen de Enajenación o Adquisición de Bienes</option>");
                $("#regimen").append("<option value='608'>Demás ingresos</option>");
                $("#regimen").append("<option value='610'>Residentes en el Extranjero sin Establecimiento Permanente en México</option>");
                $("#regimen").append("<option value='611'>Ingresos por Dividendos (socios y accionistas)</option>");
                $("#regimen").append("<option value='612'>Personas Físicas con Actividades Empresariales y Profesionales</option>");
                $("#regimen").append("<option value='614'>Ingresos por intereses</option>");
                $("#regimen").append("<option value='615'>Régimen de los ingresos por obtención de premios</option>");
                $("#regimen").append("<option value='616'>Sin obligaciones fiscales</option>");
                $("#regimen").append("<option value='621'>Incorporación Fiscal</option>");
                $("#regimen").append("<option value='625'>Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas</option>");
                
            }
        });
    });

}




function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      //Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

async function save(){
  const form_data = new FormData();

  const empresa = document.getElementById("empresa").value;
  const telefono = document.getElementById("telefono").value;
  const rfc = document.getElementById("rfc").value;
  const codigo_postal = document.getElementById("postal").value;
  const pais = document.getElementById("pais").value;
  const estado = document.getElementById("estados").value;
  const regimen = document.getElementById("regimen").value;

  form_data.append("empresa", empresa);
  form_data.append("telefono", telefono);
  form_data.append("rfc", rfc);
  form_data.append("codigo", codigo_postal);
  form_data.append("pais", pais);
  form_data.append("estado", estado);
  form_data.append("regimen", regimen);

  const url = "/profile/informacion/";

  const options = {
    method: "POST",
    body: form_data,
    headers: { "X-CSRFToken": getCookie("csrftoken") }
  }

  try {

    const response = await fetch(url, options);

    const {success} = await response.json();

    if(success){
      alert('Datos almecenados correctamente')
      window.location.href = "/validate/"
    }
    
  } catch (error) {
    console.log(error)
  }

}




function validate_form(){
  
  const errores = [];
  let codigo_postal = document.getElementById("postal").value;
  
  const sp_rfc = document.getElementById("span_rfc");


  REGEX_RFC = regex = /^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$/;
  if (!document.getElementById("rfc").value.match(REGEX_RFC)) {
    errores.push("El RFC ingresado es un RFC invalido.");
  }

  let expresion_rfc = new RegExp("[0-9]{5}") 
  if(!expresion_rfc.test(codigo_postal)){
    errores.push('Codigo postal invalido');
  }

  console.log(errores);


  if(errores.length == 0){
    const div = document.getElementById("div_error");

    div.style.display = "none";

    save();

  }else {

    sp_rfc.innerText = "RFC invalido"

    const div = document.getElementById("div_error");

    div.style.display = "block";
    div.textContent = "";

    for(let i=0; i < errores.length; i++ ){
        const error = document.createTextNode(errores[i]);
        const br = document.createElement("br");
        div.appendChild(error);
        div.appendChild(br);

    }


    document.querySelector("#register_form").reportValidity();

  }
}




