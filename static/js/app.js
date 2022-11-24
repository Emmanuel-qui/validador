// Funcion para obtener el token

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

const enviar = document.getElementById("form_button");

function send() {
  // seleccionamos los elementos de la tabla.
  const td_estruc = document.getElementById("td_estruc");
  const td_sello = document.getElementById("td_sello");
  const td_sesat = document.getElementById("td_sesat");
  const td_error = document.getElementById("td_error");

  const contenedor_tabla = document.getElementById("content_response");

  // Asignamos la url que va a realizar el proceso.
  const url = "http://127.0.0.1:8000/validate/";
  // Obtenemos el archivo enviado
  let input_file = document.getElementById("file");
  // Obtenemos los valores del formulario
  const form = new FormData();

  const file = input_file.files[0].name;

  let ext = file.split(".").pop();

  if (ext == "xml") {
    form.append("file", input_file.files[0]);
    // Utilizamos fecth para enviar el documento a nuestra vista en Django.
    fetch(url, {
      method: "POST",
      body: form,
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin",
    })
      .then((response) => response.json())
      .then((data) => {
        
        td_estruc.innerText = data.response.Estructura;
        td_sello.innerText = data.response.Sello;
        td_sesat.innerText = data.response.Sello_Sat;
        td_error.innerText = data.response.Error;
        if(data.success){
          contenedor_tabla.style.display = "block";
          document.getElementById("validate_formulario").reset();
        }
        
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  } else {
    alert("El archivo seleccionado, no es un archivo XML");
    input_file.value = "";
  }
}

enviar.addEventListener("click", send);
