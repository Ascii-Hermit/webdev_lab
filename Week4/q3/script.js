$(document).ready(function () {
  // Handle form submission
  $("#birthday-form").submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get values from the form
    const name = $("#name").val();
    const message = $("#message").val();
    const bgColor = $("#bg-color").val(); // Get the selected background color
    const fontFamily = $("#font-family").val(); // Get the selected font
    const fontSize = $("#font-size").val(); // Get the selected font size

    // Check if both fields are filled
    if (name && message) {
      // Update the card with the user's input
      $("#card-name").text(name);
      $("#card-message").text(message);

      // Apply the background color, font family, and font size
      $("#card").css("background-color", bgColor);
      $("#card").css("font-family", fontFamily);
      $("#card").css("font-size", fontSize + "px");

      // Show the generated birthday card
      $("#card").fadeIn();

      // Clear the form
      $("#name").val("");
      $("#message").val("");
    } else {
      alert("Please fill out both fields!");
    }
  });
});
