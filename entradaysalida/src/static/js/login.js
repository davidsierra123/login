
function login() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (email === "jesus@gmail.com" && password === "123") {
    window.location.href = "/fronted/menu";
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";
  }else{
    alert("Datos incorrectos")
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";
  }
}
