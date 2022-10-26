console.log("cargando");

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
  

  

  const td_estruc = document.getElementById("td_estruc");
  const td_sello = document.getElementById("td_sello");
  const td_sesat = document.getElementById("td_sesat");
  const td_error = document.getElementById("td_error");

  // Asignamos la url que va a realizar el proceso.
  const url = "http://127.0.0.1:8000/validate/";
  // Obtenemos el archivo enviado
  let input_file = document.getElementById("file");
  // Obtenemos los valores del formulario
  const form = new FormData();
  
  // var file = input_file.files[0].name;
  
  // let ext = file.split('.').pop()

  // if(ext == "xml"){
  //   alert("si es un xml")
  // }else {
  //   alert("No es un xml")
  //   input_file.value = "";
  // }


  form.append("file", input_file.files[0]);
  //form.append("csrftoken", csrftoken);

  // Utilizamos fecth para enviar el documento a nuestra vista en Django.
  fetch(url, {
    method: "POST",
    body: form,
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      td_estruc.innerText = data.Estructura;
      td_sello.innerText = data.Sello;
      td_sesat.innerText = data.Sello_Sat;
      td_error.innerText = data.Error;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

enviar.addEventListener("click", send);
