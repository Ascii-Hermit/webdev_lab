document.addEventListener("DOMContentLoaded", function () {
  let para = document.querySelectorAll(".text");
  para.forEach((p) => {
    p.addEventListener("click", function () {
      this.style.display = "none";
    });
  });
});
