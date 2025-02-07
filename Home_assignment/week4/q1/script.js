$(document).ready(function () {
  function bounce() {
    $(".ball")
      .animate({ top: "350px" }, 1000)
      .animate({ top: "0px" }, 1000, bounce);
  }

  bounce();
});
