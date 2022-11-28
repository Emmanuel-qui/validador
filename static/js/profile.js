$(document).ready(function() {
      
    $('#empresa').on("keyup",function (){
      console.log('hola');
    });
  
});

// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
// const csrftoken = getCookie("csrftoken");


// const button = document.getElementById("id_update");


// function updateAccount() {

//   const form = new FormData();

//   const empresa = document.getElementById("id_empresa").value;
//   const telefono = document.getElementById("id_telefono").value;
//   const codigo_postal = document.getElementById("id_codigo_postal").value;
//   const pais = document.getElementById("id_pais").value;
//   const estado = document.getElementById("id_estado").value;
//   const imagen = document.getElementById("id_imagen");


//   form.append("empresa", empresa);
//   form.append("telefono", telefono);
//   form.append("postal", codigo_postal);
//   form.append("pais", pais);
//   form.append("estado", estado);
//   form.append("imagen", imagen.files[0]);

//   const url = "/profile/";

//   const options = {
//     method: "POST",
//     body: form,
//     headers: { "X-CSRFToken": csrftoken },
//   };

//   fetch(url, options)
//     .then((response) => response.json())
//     .then((data) => {
//       if(data.success){
//         console.log(data);
//         window.location.reload();
//       }
      
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     });
// }


// button.addEventListener("click", updateAccount);
