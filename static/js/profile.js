// $(document).ready(function () {
//   var url = 'http://127.0.0.1:8000/profile/data/';


//   $.get(url, function (response) {
//       $("#id_tel").val(response.telefono);
//       $("#id_cp").val(response.codigo_postal);
//       $("#id_estado").val(response.pais);
//       $("#id_pais").val(response.estado);
//   });


// });

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

// const boton = document.getElementById("boton-data");

const button = document.getElementById("id_update");

// function saludar() {
//   const formulario = document.getElementById("form-datos");
//   const form = new FormData();

//   const nombre = document.getElementById("nombre").value;
//   const telefono = document.getElementById("telefono").value;
//   const rfc = document.getElementById("rfc").value;
//   const codigo_postal = document.getElementById("postal").value;
//   const pais = document.getElementById("pais").value;
//   const estado = document.getElementById("estado").value;
//   const tipo = document.getElementById("tipo_persona").value;
//   const regimen = document.getElementById("regimen").value;

//   form.append("nombre", nombre);
//   form.append("telefono", telefono);
//   form.append("rfc", rfc);
//   form.append("postal", codigo_postal);
//   form.append("pais", pais);
//   form.append("estado", estado);
//   form.append("tipo_persona", tipo);
//   form.append("regimen_fiscal", regimen);

//   const url = "http://127.0.0.1:8000/profile/";

//   const options = {
//     method: "POST",
//     body: form,
//     headers: { "X-CSRFToken": getCookie("csrftoken") },
//   };

//   fetch(url, options)
//     .then((response) => response.json())
//     .then((data) => {
//       console.log(data);
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     });
// }

function updateAccount() {

  const form = new FormData();

  const empresa = document.getElementById("id_empresa").value;
  const telefono = document.getElementById("id_telefono").value;
  const codigo_postal = document.getElementById("id_codigo_postal").value;
  const pais = document.getElementById("id_pais").value;
  const estado = document.getElementById("id_estado").value;
  const imagen = document.getElementById("id_imagen");


  form.append("empresa", empresa);
  form.append("telefono", telefono);
  form.append("postal", codigo_postal);
  form.append("pais", pais);
  form.append("estado", estado);
  form.append("imagen", imagen.files[0]);

  

  const url = "";

  const options = {
    method: "POST",
    body: form,
    headers: { "X-CSRFToken": csrftoken },
  };

  fetch(url, options)
    .then((response) => response.json())
    .then((data) => {
      if(data.success){
        console.log(data);
        window.location.reload();
      }
      
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// boton.addEventListener("click", saludar);

button.addEventListener("click", updateAccount);
