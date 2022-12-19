
async function sendEmail(){
    const send = document.getElementById("id_send");
    const url = "/validate/send/"+send.value+"";
    try {

      const response = await fetch(url);

      const { success } = await response.json();

      if(success){

        alert('Correo enviado, con exito.');
      }else {

        alert('Hubo un problema.');
      }

      
    } catch (error) {
      
      console.log(error);
    }


}



