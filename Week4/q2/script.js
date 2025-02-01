$(document).ready(function () {
  let currentInput = "";
  let previousInput = "";
  let operator = "";

  // Append numbers to the display
  $(".btn[data-value]").click(function () {
    currentInput += $(this).data("value");
    $("#result").val(currentInput);
  });

  // Set operator (+, -, *, /)
  $(".operator").click(function () {
    if (currentInput === "") return; // Do nothing if no number is entered
    if (previousInput !== "") {
      calculate(); // Calculate if there's a previous result
    }
    operator = $(this).data("op");
    previousInput = currentInput;
    currentInput = "";
  });

  // Calculate result
  $("#equals").click(function () {
    if (previousInput === "" || currentInput === "") return; // Ensure both inputs are present
    calculate();
  });

  // Clear the display
  $("#clear").click(function () {
    currentInput = "";
    previousInput = "";
    operator = "";
    $("#result").val("");
  });

  // Perform the calculation based on the operator
  function calculate() {
    let result;
    const prev = parseFloat(previousInput);
    const current = parseFloat(currentInput);

    if (isNaN(prev) || isNaN(current)) return; // Ensure both values are valid numbers

    switch (operator) {
      case "+":
        result = prev + current;
        break;
      case "-":
        result = prev - current;
        break;
      case "*":
        result = prev * current;
        break;
      case "/":
        if (current === 0) {
          alert("Cannot divide by zero!");
          clearResult();
          return;
        }
        result = prev / current;
        break;
      default:
        return;
    }

    currentInput = result.toString();
    operator = "";
    previousInput = "";
    $("#result").val(currentInput);
  }
});
