
const enlace = document.getElementById("id_send");


function email(){
    const id = enlace.value;
    const url = "http://127.0.0.1:8000/validate/send/"+id+"";
    fetch(url, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          alert(data.msj);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
}


enlace.addEventListener("click", email);