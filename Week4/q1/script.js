$(document).ready(function () {
  let moved = false;

  $("#move-button").click(function () {
    if (moved == true) {
      $("#content-wrapper").css("transform", "translateX(100%)");
      moved = false;
    } else {
      $("#content-wrapper").css("transform", "translateX(-100%)");
      moved = true;
    }
  });
});
