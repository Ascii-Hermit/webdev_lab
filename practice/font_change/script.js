// let subButton = document.getElementById("button");

// subButton.addEventListener("click", function () {
//   let fontSize = document.getElementById("font-size").value; // Get value from input
//   if (fontSize) {
//     // Ensure the input is not empty
//     document.getElementById("text").style.fontSize = fontSize + "px"; // Append 'px' and apply
//   }
// });

$(document).ready(function () {
  $("#button").click(function () {
    let fontSize = $("#font-size").val();
    $("#text").css("font-size", fontSize + "px");
  });
});
