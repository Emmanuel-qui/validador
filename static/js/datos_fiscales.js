$(document).ready(function() {
      validate_input();

      select_regimen();
});

function validate_input() {
      // validar nombre de la empresa.
      $("#empresa").keypress(function(event) {
          if ((event.charCode < 65 || event.charCode > 90) && (event.charCode < 97 || event.charCode > 122) && (event.charCode != 32)) {
              return false;
          }
      });
      // validar numero de telefono
      $('#telefono').mask('(000) 000-0000');
      // validar rfc
      $("#rfc").keypress(function(event) {
          if ((event.charCode < 65 || event.charCode > 90) && (event.charCode < 48 || event.charCode > 57)) {
              return false;
          }
      });
      $("#rfc").keyup(function(event) {
          var caracteres = $(this).val().length;

          if(caracteres == 13){
            $(this).keypress(function(event){ return false })
          }
      })


      // validando Codigo Postal.
      $("#postal").keypress(function(event){
        if((event.charCode < 65 || event.charCode > 90) && (event.charCode < 97 || event.charCode > 122) && (event.charCode < 48 || event.charCode > 57)){
          return false;
        }
        
      });

      $("#postal").keyup(function(event){

          var caracteres = $(this).val().length;

          if(caracteres == 5){
            $(this).keypress(function(event){ return false })
          }
      });

      // validando pais.
      $("#pais").keypress(function (event){
        var regex = new RegExp("^[a-zA-Z\u00C0-\u017F\s]+$");
        var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
        if (!regex.test(key)) {
          event.preventDefault();
          return false;
       }

      });

      $("#pais").keyup(function (event){

          var mx = "México";

          if($(this).val() == mx){
            $("#label_estado").css("display", "none");

            $("#estado").css("display", "none");
            
            $("#estados_mexicanos").css("display","block");
          }

          if($(this).val() == ""){
            $("#estado").css("display", "block");
            $("#label_estado").css("display", "block");
            $("#estados_mexicanos").css("display","none");
          }
      });

      $("#pais").keyup(function (event){

          var regex = new RegExp("^A-Z");
          var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
          if (!regex.test(key)) {
            
            $("#span_pais").html("Debe empezar con una letra mayuscula");
          }

          if($("#pais").val() == "") {
            $("#span_pais").html("Pais");
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

async function save(){
  const form_data = new FormData();

  const empresa = document.getElementById("empresa");
  const telefono = document.getElementById("telefono");
  const rfc = document.getElementById("rfc");
  const codigo_postal = document.getElementById("postal");
  const pais = document.getElementById("pais");
  const estado = document.getElementById("estado");
  const regimen = document.getElementById("regimen");

  form_data.append("empresa", empresa);
  form_data.append("telefono", telefono);
  form_data.append("rfc", rfc);
  form_data.append("codigo", codigo_postal);
  form_data.append("pais", pais);
  form_data.append("estado", estado);
  form_data.append("regimen", regimen);


  try {

    
  } catch (error) {
    console.log(error)
  }



}
