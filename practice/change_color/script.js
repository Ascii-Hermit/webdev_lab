document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("#card input[type='radio']").forEach((button) => {
    button.addEventListener("change", function () {
      document.getElementById("bg-display").style.backgroundColor = this.value;
    });
  });
});
