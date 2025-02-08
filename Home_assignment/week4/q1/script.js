// $(document).ready(function () {
//   function bounce() {
//     $(".ball")
//       .animate({ top: "350px" }, 1000)
//       .animate({ top: "0px" }, 1000, bounce);
//   }

//   bounce();
// });

document.addEventListener("DOMContentLoaded", function () {
  function bounce() {
    let ball = document.querySelector(".ball");
    ball.animate([{ top: "0px" }, { top: "350px" }, { top: "0px" }], {
      duration: 2000,
      iterations: Infinity,
    });
  }
  bounce();
});
