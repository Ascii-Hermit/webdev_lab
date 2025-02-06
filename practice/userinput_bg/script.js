$(document).ready(function () {
  //loads only after entire dom is initialised
  $("#form").submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    const name = $("#form-name").val().trim();
    const message = $("#form-message").val().trim();
    const bgColor = $("#bg-color").val();
    const fontFamily = $("#font-family").val();
    const fontSize = parseInt($("#font-size").val(), 10); // very important

    if (name && message) {
      $("#card-name").text(name);
      $("#card-message").text(message);

      $("#generated-card").css({
        "background-color": bgColor,
        padding: "20px",
        "border-radius": "10px",
        display: "block",
      });

      $("#card-content h2, #card-content p").css({
        "font-family": fontFamily,
        "font-size": fontSize + "px",
      });

      $("#generated-card").fadeIn();

      $("#form-name, #form-message, #font-size").val("");
      $("#bg-color").val("#FFFFFF");
      $("#font-family").prop("selectedIndex", 0);
    } else {
      alert("Please fill out both fields!");
    }
  });
});
