

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
//const csrftoken = getCookie("csrftoken");

const boton = document.getElementById("boton-data");

function saludar() {
    
    const formulario = document.getElementById("form-datos");
    const form = new FormData();

    const nombre = document.getElementById("nombre").value;
    const telefono = document.getElementById("telefono").value;
    const rfc = document.getElementById("rfc").value;
    const codigo_postal = document.getElementById("postal").value;
    const pais = document.getElementById("pais").value;
    const estado = document.getElementById("estado").value;
    const tipo = document.getElementById("tipo_persona").value;
    const regimen = document.getElementById("regimen").value;

    form.append("nombre", nombre);
    form.append("telefono", telefono);
    form.append("rfc", rfc);
    form.append("postal", codigo_postal);
    form.append("pais", pais);
    form.append("estado", estado);
    form.append("tipo_persona", tipo);
    form.append("regimen_fiscal", regimen);

    const url = "http://127.0.0.1:8000/profile/";

    const options = {
        method: "POST",
        body: form,
        headers: { "X-CSRFToken": getCookie("csrftoken") },
       
      };

    fetch(url, options)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        })
    .catch((error) => {
      console.error("Error:", error);
    });
}


boton.addEventListener("click",saludar);