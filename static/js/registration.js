
let registrationLi = document.getElementById("registration");
registrationLi.dataset.toggle = "modal";
registrationLi.dataset.target = "#registrationModal";


$(document).ready(function () {
  $("#registerButton").click(function () {
    $("#registerForm").submit();
  });
});
