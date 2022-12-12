
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

