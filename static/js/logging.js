
let loggingLi = document.getElementById("logging");
loggingLi.dataset.toggle = "modal";
loggingLi.dataset.target = "#loggingModal";


$(document).ready(function () {
  $("#loggingButton").click(function () {
    $("#loggingForm").submit();
  });
});
