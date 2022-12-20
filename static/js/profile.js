window.onload = () => {
  console.log('Cargando')
  getState()
  validate_input()
}

function validate_input() {
  
  // validar numero de telefono
  $('#id_telefono').mask('(000) 000-0000');

  // validando Codigo Postal.
  $("#id_codigo_postal").keypress(function(event){
    if(event.charCode < 48 || event.charCode > 57){
      return false;
    }
    
  });

  $("#id_codigo_postal").keyup(function(event){

      var caracteres = $(this).val().length;

      if(caracteres == 5){
        $(this).keypress(function(event){ return false })
      }
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

async function getState(){
  const estados = ['AGS','BC','BCS','CAMP','COAH','COL','CHIS','CHIH','DF','DGO','GTO','GRO','HGO','JAL','MEX','MICH','MOR',
  'NAY','NL','OAX','PUE','QRO','QR','SLP','SIN','SON','TAB','TAMS','TLAX','VER','YUC','ZAC']

  let position = 0;

  try {

    const response = await fetch("/profile/data/");

    const {estado} = await response.json() 
    
    console.log(estado)

    for(let i=0; i<=estados.length; i++){
      if(estados[i]==estado){
        console.log(i)
        position = i
      }
    }

    const select = document.getElementById("id_estado").options[position];
    select.setAttribute("selected","selected");
    
  } catch (error) {
    console.log(error)
  }
  


}

async function updatePhoto() {
  const url = "/profile/";
  const form = new FormData();

  const empresa = document.getElementById("id_empresa").value;
  const telefono = document.getElementById("id_telefono").value;
  const codigo_postal = document.getElementById("id_codigo_postal").value;
  const pais = document.getElementById("id_pais").value;
  const estado = document.getElementById("id_estado").value;
  const imagen = document.getElementById("id_imagen");

  const path = imagen.value;

  const extensiones = /(.jpg|.jpeg|.png|.gif)$/i;


  if (extensiones.exec(path)) {

    form.append("empresa", empresa);
    form.append("telefono", telefono);
    form.append("postal", codigo_postal);
    form.append("pais", pais);
    form.append("estado", estado);
    form.append("imagen", imagen.files[0]);

    const options = {
      method: "POST",
      body: form,
      headers: { "X-CSRFToken": getCookie("csrftoken") }
    };

    try {
      const response = await fetch(url, options);

      const data = await response.json();

      console.log(data);

      if (data.success) {

        alert('Imagen actualizada');
        window.location.reload();
      }

    } catch (error) {
      console.log(error)
    }

  }else {

    alert('El archivo cargado no es una imagen.');
    imagen.value = "";
  }


}

async function updateUser() {
 

  const url = "/profile/";

  const form = new FormData();

  const empresa = document.getElementById("id_empresa").value;
  const telefono = document.getElementById("id_telefono").value;
  const codigo_postal = document.getElementById("id_codigo_postal").value;
  const pais = document.getElementById("id_pais").value;
  const estado = document.getElementById("id_estado").value;

  form.append("empresa", empresa);
  form.append("telefono", telefono);
  form.append("postal", codigo_postal);
  form.append("pais", pais);
  form.append("estado", estado);

  const options = {
    method: "POST",
    body: form,
    headers: { "X-CSRFToken": getCookie("csrftoken") }
  };

  try {

    const response = await fetch(url, options);

    const data = await response.json();

    console.log(data);

    if (data.success) {

      alert('Datos Actualizados');
      window.location.reload();
    }

  } catch (error) {

    console.log(error);
  }


}


function validate_form(){

  const empresa = document.getElementById("id_empresa").value;
  const telefono = document.getElementById("id_telefono").value;
  const codigo_postal = document.getElementById("id_codigo_postal").value;
  const pais = document.getElementById("id_pais").value;
  const estado = document.getElementById("id_estado").value;
  let expresion_rfc = new RegExp("[0-9]{5}") 

  if(empresa=="" || telefono=="" || codigo_postal==""){
    alert("Ningun campo debe estar vació, verfique los campos")
  }else if(!expresion_rfc.test(codigo_postal)){
    alert("El codigo postal es invalido")

  }else{
    
    updateUser();
  }
  

}
