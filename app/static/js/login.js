window.addEventListener("DOMContentLoaded", function () {
  var popup = document.getElementById("popup-message");
  if (popup) {
    popup.style.display = "block";
    setTimeout(function () {
      popup.style.display = "none";
    }, 1500);
  }
});