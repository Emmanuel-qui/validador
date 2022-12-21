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



async function send() {

  const td_estruc = document.getElementById("td_estruc");
  const td_sello = document.getElementById("td_sello");
  const td_sesat = document.getElementById("td_sesat");
  const td_error = document.getElementById("td_error");

  const contenedor_tabla = document.getElementById("content_response");
  
  const input_file = document.getElementById("id_file");  

  const file = input_file.files[0].name;

  const ext = file.split(".").pop();

    if (ext == "xml" || ext == "XML") {

      const form = new FormData();
      form.append("file", input_file.files[0]);
    

      try {

        const url = "/validate/";
          
        const options = {
          method: "POST",
          body: form,
          headers: { "X-CSRFToken": csrftoken },
          mode: "same-origin",
        }

        const response = await fetch(url, options);

        const data = await response.json();

        console.log(data);

        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
          }
        })
        
        Toast.fire({
          icon: 'success',
          title: 'Validación exitosa!'
        })

        td_estruc.innerText = data.Estructura;
        td_sello.innerText = data.Sello;
        td_sesat.innerText = data.Sello_Sat;
        td_error.innerText = data.Error;
        contenedor_tabla.style.display = "block";
        document.getElementById("validate_formulario").reset();
        

      } catch (error) {
        
        console.error(error);

      }
      
  } else {
    alert("El archivo seleccionado, no es un archivo XML");
    input_file.value = "";
  }

}


