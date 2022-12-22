async function sendEmail(){
    const send = document.getElementById("id_send");
    const url = "/validate/send/"+send.value+"";
    try {

      const response = await fetch(url);

      const { success, email } = await response.json();

      if(success){
        Swal.fire(
          'Email enviado!',
          'Enviadio al correo '+email+'',
          'success'
        )
      }else {
        Swal.fire(
          'Ocurrio un error',
          '¡Intentelo más tarde!',
          'error'
        )
      }

      
    } catch (error) {
      
      console.log(error);
    }


}



