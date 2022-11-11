
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

    form.append("nombre", nombre);
    form.append("telefono", telefono)

    console.log(form);

    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(form)
      };

    fetch("/robots.txt", options)
        .then(response => {
           console.log(response);
        }).then(data => {
            console.log(data)
        })
    
    
}

boton.addEventListener("click",saludar);